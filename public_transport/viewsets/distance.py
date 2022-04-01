import psycopg2
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from public_transport.models import Stop
from public_transport.serializers import StopSerializer


# def check_schema(conf):
#     age_schema = 

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
        
        #TODO SCHEMA
        match request.data["age"]:
            case num if num in range(0, 15) or num in range(36, 50):
                relevant_distance = 1
            case num if num in range(16, 25):
                relevant_distance = 5
            case num if num in range(16, 25):
                relevant_distance = 2
            case num if num in range(51, 65):
                relevant_distance = 0.5
            case num if num in range(65, 120):
                relevant_distance = 0.1
            case _:
                relevant_distance = 10
            
                
        
        conn = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="db",
                                port="5432",
                                database="postgres")
        cur = conn.cursor()

        # psql_query = "select (point(-0.1277,51.5073) <@> point(-74.006,40.7144)) as distance"
        # psql_query = "SELECT TOP 5 FROM  (point(-0.1277,51.5073) <@> point(-74.006,40.7144)) as distance"
        # WHERE (point(longitude,latitude) <@> point({request.data["longitude"]},{request.data["latitude"]})) < {relevant_distance} 
        psql_query = f"""
        SELECT * 
        FROM public_transport_stop 
        WHERE (point(longitude,latitude) <@> point({request.data["longitude"]},{request.data["latitude"]})) < {relevant_distance}
        ORDER BY (point(longitude,latitude) <@> point({request.data["longitude"]},{request.data["latitude"]}))
        ASC LIMIT 5"""
        cur.execute(psql_query)
        result = cur.fetchall()

        for row in result:
            print(row)
            
        return HttpResponse(result)