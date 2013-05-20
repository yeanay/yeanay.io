import urllib2
import json
import sys

import time

from django.conf import settings
from ideology.models import Legislator

NYT_KEY = settings.NYT_KEY

def get_leg_icpsr(bioguideid):
    """Takes a bioguide ID, returns ICPSR"""
    url = 'http://api.nytimes.com/svc/politics/v3/us/legislative/congress/members/{0}.json?api-key={1}'.format(bioguideid, NYT_KEY)
    f = urllib2.urlopen(url)
    content = f.read()
    dict_response = json.loads(content)
    return dict_response['results'][0]['icpsr_id']

def replace_missing_icpsr():
    no_icpsr = Legislator.objects.filter(icpsrid = '')
    print 'Gathering {0} missing ICPSR IDs from NYT API'.format(len(no_icpsr))
    for c, leg in enumerate(no_icpsr):
        sys.stdout.write('\r{0} icpsr gathered'.format(c+1))
        sys.stdout.flush()
        try:
            icpsr = get_leg_icpsr(leg.bioguideid)
            leg.icpsrid = icpsr
            leg.save()
        except urllib2.HTTPError:
            print "Could not get ICPSR for {0}: {1}".format(leg.lastname, leg.bioguideid)
        time.sleep(2)

if __name__ == '__main__':
    replace_missing_icpsr()