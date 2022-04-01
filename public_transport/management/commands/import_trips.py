import csv
import os

from public_transport.models import Stop, Trip
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports trips.csv data into database'
    
    @staticmethod
    def handle(*args, **kwargs):

        all_trips = Trip.objects.all()
        print(all_trips)

        with open(os.path.join(os.getcwd(), "csv_files/trips.csv")) as f:
            reader = csv.reader(f)
            for row in reader:

                _, created = Trip.objects.get_or_create(
                    route_id=row[0],
                    service_id=row[1],
                    trip_id=row[2],
                    headsign=row[3],
                    direction_id=row[4],
                    shape_id=row[5],
                    brigade_id=row[6],
                    vehicle_id=row[7],
                    variant_id=row[8],
                )

        all_trips = Trip.objects.all()
        print(all_trips)
