import csv
import os

from public_transport.models import Trip, Route
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports trips.csv data into database'
    
    @staticmethod
    def handle(*args, **kwargs):
        
        all_trips = Trip.objects.all()
        print(all_trips)

        with open(os.path.join(os.getcwd(), "csv_files/trips.csv"), encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            next(reader, None)
            for row in reader:
                if not Route.objects.filter(id=row[0]).exists():
                    raise Exception(f"There is no route with id {row[0]}")

                route_id = Route.objects.get(id=row[0])

                _, created = Trip.objects.get_or_create(
                    route_id=route_id,
                    service_id=row[1],
                    trip_id=row[2],
                    headsign=row[3],
                    direction_id=row[4]
                )

        all_trips = Trip.objects.all()
        print(all_trips)
