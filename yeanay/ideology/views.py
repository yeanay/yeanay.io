from django.http import HttpResponse
from ideology.models import Ideology, Legislator, LegislatorSession
from django.db.models import Avg

import json

def congress(request, congress_num, cham):
    full_congress = Ideology.objects.filter(congress=congress_num,
                    chamber=cham)
    json_dict = []
    print len(full_congress)
    for mem in full_congress:
        json_dict.append({'name': mem.name,
                         'district': mem.district,
                         'party_id': mem.party_id,
                         'state_id': mem.state_id,
                         'congress': mem.congress,
                         'ideology': mem.first_dimension})
    return HttpResponse(json.dumps(json_dict), mimetype="application/json")

def polarization_over_time(request):
    """Returns JSON of polarization (distance between republicans and
    dems over time)"""
    party_avgs = Ideology.objects.values('congress', 'chamber', 'party_id') \
                                 .annotate(party_avg = Avg('first_dimension')) \
                                 .filter(party_id__in = [100, 200]) \
                                 .order_by('congress', 'chamber', 'party_id').all()
    polarization_dict = []
    polar_grps = [(party_avgs[x], party_avgs[x+1]) for x in range(0, len(party_avgs), 2)]
    for dem, rep in polar_grps:
        polar = {}
        polar['chamber'] = dem['chamber']
        polar['congress'] = dem['congress']
        polar['polarization'] = rep['party_avg'] - dem['party_avg']
        polarization_dict.append(polar)
    json_result = json.dumps(polarization_dict)
    return HttpResponse(json_result, mimetype="application/json")
