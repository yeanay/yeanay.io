from django.http import HttpResponse
from ideology.models import ideology

import json
def congress(request, congress_num, cham):
    full_congress = ideology.objects.filter(congress=congress_num,
                    chamber=cham)
    json_dict = []
    print len(full_congress)
    for mem in full_congress:
        json_dict.append({'name': mem.name,
                         'district': mem.district,
                         'party_id': mem.party_id,
                         'state_id': mem.state_id,
                         'congress': mem.congress})
    return HttpResponse(json.dumps(json_dict))