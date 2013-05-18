from django.core.management.base import BaseCommand, CommandError
from ideology.models import legislator_session, legislator
from django.conf import settings

import os, sys

from lxml import etree as et

xml_leg_dict = {
    'id':'govtrackid',
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
        return files

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
        if legislator.objects.filter(govtrackid=leg_dict['govtrackid']).exists():
            pass
        else:
            new_leg = legislator(**leg_dict)
            new_leg.save()
        new_sess = legislator_session(**sess_dict)
        new_sess.save()

    def handle(self, *args, **options):
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
        sys.stdout.write('Done!\n')
        sys.stdout.flush()