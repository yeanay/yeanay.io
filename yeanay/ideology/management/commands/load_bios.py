from django.core.management.base import BaseCommand, CommandError
from ideology.models import ideology
from django.conf import settings


from lxml import etree as et

class Command(BaseCommand):
    def list_bio_xml():
        """Lists bioguide XML files from govtrack"""
        pass

    def parse_xml():
        """Parses a given XML file into a list of
        dictionaries"""
        pass

    def load_to_db():
        """Loads a python dictionary of bio data into
        database"""
        pass

tree = et.parse('./data/bios/')