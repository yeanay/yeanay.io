from django.core.management.base import BaseCommand, CommandError
from ideology.models import LegislatorSession, Legislator
from django.conf import settings

from nyt_api import *
import time
import os, sys

from lxml import etree as et

xml_leg_dict = {
    'id':'govtrackid',
    'icpsrid':'icpsrid',
    'lastname': 'lastname',
    'firstname': 'firstname',
    'birthday': 'birthday',
    'gender': 'gender',
    'pvsid': 'pvsid',
    'bioguideid': 'bioguideid',
    'youtubeid': 'youtubeid',
    'twitterid': 'twitterid',
    'facebookgraphid': 'facebookid',
    'thomasid': 'thomasid',
}

xml_sess_dict = {
    'id': 'govtrackid',
    'type': 'chamber',
    'district': 'district',
    'startdate': 'startdate',
    'enddate': 'enddate',
    'party': 'party',
    'state': 'state',
    'session': 'session'
}

class Command(BaseCommand):
    def list_bio_xml(self):
        """Lists bioguide XML files from govtrack"""
        files = os.listdir('data/bios/')
        filtered = filter(lambda x: x[-3:]=='xml', files)
        return filtered

    def parse_xml(self, f):
        """Parses a given XML file into a list of
        dictionaries"""
        path = 'data/bios/'
        tree = et.parse('{0}{1}'.format(path, f))
        session = tree.xpath('//people')[0].values()[0]
        people = tree.xpath('//person')
        dict_list = []
        for person in people:
            person_dict = dict((e[0], e[1]) for e in person.items())
            session_info = person.xpath('./role')[0]
            sess_dict = dict((e[0], e[1]) for e in session_info.items())
            for k, v in sess_dict.items():
                person_dict[k] = v
            person_dict['session'] = session
            dict_list.append(person_dict)
        return dict_list

    def create_dicts(self, person_dict):
        """Takes a person's dictionary, returns dict able to be
        passed as an argument when creating models for DB"""
        leg_dict = {}
        sess_dict = {}
        dates = ['birthday', 'startdate', 'enddate']
        for k, v in xml_leg_dict.items():
            if k in person_dict:
                leg_dict[v] = person_dict[k]
            elif k in dates:
                leg_dict[v] = None
            else:
                leg_dict[v] = ''

        for k, v in xml_sess_dict.items():
            if k in person_dict:
                sess_dict[v] = person_dict[k]
            elif v == 'district':
                sess_dict[v] = 0
            elif v in dates:
                sess_dict[v] = None
            else:
                sess_dict[v] = ''
        return leg_dict, sess_dict

        
    def load_to_db(self, person_dict):
        """Loads a python dictionary of bio data into
        database"""
        leg_dict, sess_dict = self.create_dicts(person_dict)
        if Legislator.objects.filter(govtrackid=leg_dict['govtrackid']).exists():
            new_leg = Legislator.objects.get(govtrackid=leg_dict['govtrackid'])
        else:
            new_leg = Legislator(**leg_dict)
            new_leg.save()
        new_sess = LegislatorSession(legislator=new_leg, **sess_dict)
        new_sess.save()

    def replace_missing_icpsr(self):
        f = open('./data/bioguide_to_icpsr.csv')
        bioguides = f.readlines()
        for bio in bioguides:
            bio = bio.rstrip()
            name, bio_id, icpsr = bio.split(',')
            bio_id = bio_id.strip()
            icpsr = icpsr.strip()
            leg = Legislator.objects.filter(bioguideid=bio_id).reverse()[0]
            leg.icpsrid = icpsr
            leg.save()
        
        
    def handle(self, *args, **options):

        ## Delete Existing Data (removes chance of duplicates) ##
        Legislator.objects.all().delete()
        LegislatorSession.objects.all().delete()
        
        files = self.list_bio_xml()
        bios = []
        for f in files:
            bios += self.parse_xml(f)
        print "There are {0} bios to load into the databases".format(len(bios))
        print "Loading Bios!"
        for counter, b in enumerate(bios):
            sys.stdout.write('\rAdded {0} bios so far'.format(counter))
            sys.stdout.flush()
            self.load_to_db(b)
        sys.stdout.write('\nDone!\n')
        sys.stdout.flush()

        print "Loading Missing ICPSR IDs"
        self.replace_missing_icpsr()

        no_icpsr = Legislator.objects.filter(icpsrid = '')
        print 'Gathering {0} missing ICPSR IDs from NYT API'.format(len(no_icpsr))
        for c, leg in enumerate(no_icpsr):
            sys.stdout.write('\r{0} icpsr gathered'.format(c+1))
            sys.stdout.flush()
            icpsr = get_leg_icpsr(leg.bioguideid)
            leg.icpsrid = icpsr
            leg.save()
            time.sleep(1)