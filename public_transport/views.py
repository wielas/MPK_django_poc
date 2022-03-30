import json

from public_transport.models import City, Route
from django.core.serializers import serialize
from django.http import HttpResponse


def cities(request):
    """ View returning all cities """

    all_cities = City.objects.all()
    return HttpResponse(all_cities)


def wroclaw_routes(request):
    """ View returning all wroclaw routes """

    routes_serialized = serialize('json', Route.objects.all(), indent=4)
    clean_routes = [entry["fields"] for entry in json.loads(routes_serialized)]
    clean_routes_json = json.dumps(clean_routes, indent=4, ensure_ascii=False)

    return HttpResponse(clean_routes_json, content_type="application/json")
