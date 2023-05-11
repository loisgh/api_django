from django.http import JsonResponse
from namesapi.models import Names
from namesapi.utils import serialize_names

def test_response(request):
    return JsonResponse({
        'name': 'Lois J. Greene-Hernandez',
        'age': 62,
        'address1': '3996 44th Street',
        'address2': '',
        'city': 'Sunnyside',
        'state': 'NY',
        'zip': '11104'

    })


def get_name(request, id):
    result = Names.objects.get(id=id)
    res = {}
    if result:
        res = serialize_names(result)
    return JsonResponse(res)




