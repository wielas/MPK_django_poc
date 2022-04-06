import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from schema import And, Optional, Schema, SchemaError

from public_transport.models import Stop
from public_transport.serializers import StopSerializer
from public_transport.utils import get_distance_between_coords, stops_by_distance_query


def check_schema(conf):
    """
    Function validating post request data

    Args:
        conf (dict): data received in request
        
    Raises:
        NotAcceptable: validation unsuccessful
    """
    input_schema = Schema({Optional('age'): And(lambda n : 0 <= n <= 120, int),
                         'longitude': And(lambda n : -180 <= n <= 180, float),
                         'latitude': And(lambda n : -180 <= n <= 180, float),
                         Optional('time'): str,
                         Optional('dest_long'): And(lambda n : -180 <= n <= 180, float),
                         Optional('dest_lat'): And(lambda n : -180 <= n <= 180, float),
                         })
    try:
        input_schema.validate(conf)
    except SchemaError:
        raise NotAcceptable("Wrong request format")




class DistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns up to 5 closest stops based on user age and given coordinates
    """
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(name="testname")


    def create(self, request, *args, **kwargs):
        
        check_schema(request.data)
        
        if "age" in request.data:
            match request.data["age"]:
                case num if num in range(0, 16) or num in range(36, 50):
                    relevant_distance = 1
                case num if num in range(17, 26):
                    relevant_distance = 5
                case num if num in range(27, 51):
                    relevant_distance = 2
                case num if num in range(52, 66):
                    relevant_distance = 0.5
                case num if num in range(66, 121):
                    relevant_distance = 0.1
                case _:
                    relevant_distance = 10
        
        else:
            relevant_distance = 10
        
        closest_stops = stops_by_distance_query(request.data["longitude"], request.data["latitude"], relevant_distance)
        stops_obj_list = [get_object_or_404(Stop, id=row[0]) for row in closest_stops]

        # time handling
        if "time" not in request.data:
            return HttpResponse(json.dumps(stops_obj_list))
        
        dt_time = datetime.strptime(request.data["time"], "%H:%M:%S").time()
        # TODO filter all
        stops_gte_time = stops_obj_list[1].stoptimes_set.filter(departure_time__gte=dt_time)

        # direction handling
        if "dest_long" not in request.data or "dest_lat" not in request.data:
            print(stops_gte_time)
            
            return HttpResponse(stops_gte_time)
        
        for stop in stops_obj_list:
            print(stop)
        

                        

                        
        return HttpResponse(stops_gte_time)