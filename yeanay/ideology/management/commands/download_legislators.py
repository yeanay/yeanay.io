from django.core.management.base import BaseCommand, CommandError
from ideology.models import ideology
from django.conf import settings

import urllib2
import os

class Command(BaseCommand):
    """
    Downloads legislator biographical data.
    """
    args = '<none>'
    help = 'Downloads legislator biographical data from GovTrack.us.'

    
    
    def handle(self, *args, **options):
        try:
            os.mkdir('./data/bios/')
        except os.OSError:
            pass
        for congress in range(82, 113):
            page = urllib2.urlopen('http://www.govtrack.us/data/us/{0}/people.xml'.format(congress))
            bio_xml = page.read()
            output = open("./data/bios/bio_{0}.xml".format(congress), "w")
            output.write(bio_xml)