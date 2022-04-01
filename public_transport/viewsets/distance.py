import psycopg2
import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.response import Response
from schema import And, Optional, Schema, SchemaError

from public_transport.models import Stop
from public_transport.serializers import StopSerializer


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
                         Optional('direction'): int,
                         Optional('time'): str
                         })
    try:
        input_schema.validate(conf)
    except:
        raise NotAcceptable("Wrong request format")


def db_distance_query(data, relevant_distance):
    """
    Function returning up to 5 closest stops based on given coordinates and radius

    Args:
        data (dict): data received in request
        relevant_distance (int): acceptable distance from nearest stop measured in kilometers
    """
    
    conn = psycopg2.connect(user="postgres",
                            password="postgres",
                            host="db",
                            port="5432",
                            database="postgres")
    cur = conn.cursor()

    psql_query = f"""
    SELECT * 
    FROM public_transport_stop 
    WHERE (point(longitude,latitude) <@> point({data["longitude"]},{data["latitude"]})) < {relevant_distance}
    ORDER BY (point(longitude,latitude) <@> point({data["longitude"]},{data["latitude"]}))
    ASC LIMIT 5"""
    
    cur.execute(psql_query)
    return cur.fetchall()
    

class DistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that returns up to 5 closest stops based on user age and given coordinates
    """
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    def get_queryset(self):
        return self.queryset.filter(name="testname")


    def create(self, request, *args, **kwargs):
        print(request.data)
        
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
        
        
        closest_stops = db_distance_query(request.data, relevant_distance)
        stops_obj_list = [get_object_or_404(Stop, id=row[0]) for row in closest_stops]

        #time handling
        dt = datetime.datetime.strptime("21:00:00", "%H:%M:%S").time()
        print(stops_obj_list[0].stoptimes_set.filter(departure_time__lt=dt))
                        
        return HttpResponse(stops_obj_list[0].stoptimes_set.filter(departure_time=dt))