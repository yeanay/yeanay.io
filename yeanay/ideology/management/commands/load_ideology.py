from django.core.management.base import BaseCommand, CommandError
from ideology.models import ideology
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
            if obs['congress'] < 80:
                continue
            leg = ideology()
            leg.congress = obs['congress']
            leg.icpsr_id = obs['icpsr_id']
            leg.state_id = obs['state_code']
            leg.district = obs['cd']
            leg.name = obs['name']
            leg.party_id = obs['party_code']
            leg.first_dimension = obs['first_dimension']
            leg.second_dimension = obs['second_dimension']
            leg.chamber = chamber
            leg.save()
            
    def handle(self, *args, **options):
        if len(args) != 0:
            raise CommandError('No arguments taken for command')

        # Delete existing ideology entries #
        ideology.objects.all().delete()

        # Read in CSV file from Data Folder #
        house_file = open('./data/house_ideology.csv', 'r')
        house_csv = csv.DictReader(house_file)
        senate_file = open('./data/senate_ideology.csv', 'r')
        senate_csv = csv.DictReader(senate_file)

        self.stdout.write('Loading House of Representatives\n')
        self.csv_loader(house_csv, 'house')

        self.stdout.write('Loading Senate\n')
        self.csv_loader(senate_csv, 'senate')