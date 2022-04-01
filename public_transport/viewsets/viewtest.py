import psycopg2
from django.views import View
from django.http import HttpResponse


class DistanceView(View):
    def get(self, request):
        # print(request)
        conn = psycopg2.connect(user="postgres",
                                password="postgres",
                                host="db",
                                port="5432",
                                database="postgres")
        cur = conn.cursor()

        psql_query = "select (point(-0.1277,51.5073) <@> point(-74.006,40.7144)) as distance"
        cur.execute(psql_query)
        result = cur.fetchall()

        for row in result:
            print(row)
        return HttpResponse(result[0])

    def post(self, request, *args, **kwargs):
        print(request)
        print(request.POST)
        print(args)
        print(kwargs)
        return HttpResponse("ppppposted")