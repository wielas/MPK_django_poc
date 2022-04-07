import json
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from schema import And, Optional, Schema, SchemaError

from public_transport.models import Stop
from public_transport.serializers import StopSerializer, StopTimesSerializer
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

    def list(self, request, *args, **kwargs):
        print(request.GET.get('q', ''))
        
        age = request.GET.get('age', '20')
        longitude = request.GET.get('long', 17.019393880)
        latitude = request.GET.get('lat', 51.1071331900)
        time = request.GET.get('time', '')
        
        self.create(request, age=age, longitude=longitude, latitude=latitude, time=time)
        return HttpResponse("get resp")
        
    def create(self, request, *args, **kwargs):
        
        if not kwargs:
            check_schema(request.data)
        
        age_to_match = request.data["age"] if "age" not in kwargs or not kwargs["age"] else kwargs["age"]
        print(age_to_match)
        if "age" in request.data:
            match age_to_match:
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

        long = request.data["longitude"] if "longitude" not in kwargs or not kwargs["longitude"] else kwargs["longitude"]
        lat = request.data["latitude"] if "latitude" not in kwargs or not kwargs["latitude"] else kwargs["latitude"]
        
        closest_stops = stops_by_distance_query(request.data["longitude"], request.data["latitude"], relevant_distance)
        stops_obj_list = [get_object_or_404(Stop, id=row[0]) for row in closest_stops]


        # time handling
        if "time" not in request.data:
            return HttpResponse(stops_obj_list)

        dt_time = datetime.strptime(request.data["time"], "%H:%M:%S").time()
        
        stop_times_gte = [stop_obj.stoptimes_set.filter(departure_time__gte=dt_time) for stop_obj in stops_obj_list]
        
        stop_times_dict_list = []
        print(stop_times_gte[0][0])
        print(type(stop_times_gte))
        print(type(stop_times_gte[0]))
        
        for stop in range(len(stop_times_gte)):
            dep_times = [str(item[0]) + " " + str(item[1]) for item in list(stop_times_gte[stop].values_list('departure_time', 'trip_id__headsign'))]
            
            stop_times_dict_list.append({
                "stop_name": stops_obj_list[stop].name,
                # "vehicle headsign": stops_obj_list[stop].id,
                "first entry route": stop_times_gte[stop].first().trip_id.route_id.description,
                "departure time /w direction": dep_times,
            })
        
        
        # direction handling
        if "dest_long" not in request.data or "dest_lat" not in request.data:
            return HttpResponse(json.dumps(stop_times_dict_list))
        
        
        
            
        return HttpResponse("route, times and headsigns")