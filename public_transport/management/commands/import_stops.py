import csv
import os

from django.core.management.base import BaseCommand
from public_transport.models import Stop, StopTimes


class Command(BaseCommand):
    help = 'Imports stops.csv data into database'
    
    @staticmethod
    def handle(*args, **kwargs):
        
        all_stops = Stop.objects.all()
        print(all_stops)

        with open(os.path.join(os.getcwd(), "csv_files/stops.csv")) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Stop.objects.get_or_create(
                    id=row[0],
                    code=row[1],
                    name=row[2],
                    latitude=row[3],
                    longitude=row[4]
                )

        all_stops = Stop.objects.all()
        print(all_stops)
