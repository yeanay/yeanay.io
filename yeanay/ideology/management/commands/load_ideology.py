from django.core.management.base import BaseCommand, CommandError
from ideology.models import Ideology, Legislator
from django.conf import settings
import csv

class Command(BaseCommand):
    """
    Loads legislator ideology data into database for every Congress after the
    80th Congress.
    """
    
    args = '<none>'
    help = 'Loads ideology for all legislators since 80th Congress'

    def csv_loader(self, csv_reader, chamber):
        """
        Helper function to load CSVs into DB
        """
        for obs in csv_reader:
            if int(obs['congress']) < 82:
                pass
            elif int(obs['cd']) == 0 and obs['state'] == 'USA':
                pass
            else:
                new_ideo = Ideology()
                new_ideo.congress = obs['congress']
                new_ideo.icpsrid = obs['icpsr_id']
                new_ideo.state_id = obs['state_code']
                new_ideo.district = obs['cd']
                new_ideo.name = obs['name']
                new_ideo.party_id = obs['party_code']
                new_ideo.first_dimension = obs['first_dimension']
                new_ideo.second_dimension = obs['second_dimension']
                new_ideo.chamber = chamber
                try:
                    legis = Legislator.objects.get(icpsrid=obs['icpsr_id'])
                    new_ideo.legislator = legis
                    new_ideo.save()
                except Legislator.DoesNotExist:
                    print "\nCould not find Legislator using ICPSR {0}".format(obs['icpsr_id'])

                    last_name = obs['name'].split(' ')[0].title()

                    print "Trying Last Name Search on {0}".format(last_name)
                    try:
                        legis = Legislator.objects.get(lastname=last_name)
                        new_ideo.legislator = legis
                        new_ideo.save()
                    except (Legislator.MultipleObjectsReturned, Legislator.DoesNotExist):
                        print "Multiple Legislators with same last name"
                        print "NAME: {0}".format(obs['name'])
                except Legislator.MultipleObjectsReturned:
                    print "Multiple legislators with icpsr id: {0}".format(obs['icpsr_id'])
            
    def handle(self, *args, **options):
        if len(args) != 0:
            raise CommandError('No arguments taken for command')

        # Delete existing ideology entries #
        Ideology.objects.all().delete()

        # Read in CSV file from Data Folder #
        house_file = open('./data/house_ideology.csv', 'r')
        house_csv = csv.DictReader(house_file)
        senate_file = open('./data/senate_ideology.csv', 'r')
        senate_csv = csv.DictReader(senate_file)

        self.stdout.write('Loading House of Representatives\n')
        self.csv_loader(house_csv, 'house')

        self.stdout.write('Loading Senate\n')
        self.csv_loader(senate_csv, 'senate')