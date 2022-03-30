import csv
import os

from public_transport.models import City, Route
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports cities.csv and routes.csv data from base folder into database'

    def handle(self, *args, **kwargs):

        # import cities.csv into City model
        all_cities = City.objects.all()
        print(all_cities)

        with open(os.path.join(os.getcwd(), "csv_files/cities.csv")) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = City.objects.get_or_create(
                    id=row[0],
                    name=row[1],
                )

        all_cities = City.objects.all()
        print(all_cities)

        # import routes-wroclaw.csv into Route model
        all_routes = Route.objects.all()
        print(all_routes)

        with open(os.path.join(os.getcwd(), "csv_files/routes-wroclaw.csv")) as f:
            reader = csv.reader(f)
            for row in reader:
                _, created = Route.objects.get_or_create(
                    id=row[0],
                    short_name=row[1],
                    description=row[2],
                )

        all_routes = Route.objects.all()
        print(all_routes)