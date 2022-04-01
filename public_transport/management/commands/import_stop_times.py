import csv
import os

from public_transport.models import Stop, StopTimes, Trip
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports stop_times.csv data into database'

    @staticmethod
    def handle(*args, **kwargs):

        with open(os.path.join(os.getcwd(), "csv_files/stop_times.csv"), encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None)
            next(reader, None)
            all_stoptimes = StopTimes.objects.all()
            print(all_stoptimes)

            for row in reader:
                # Make a relation to Stop and Trip objects

                if not Stop.objects.filter(id=row[3]).exists():
                    raise Exception(f"There is no stop with id {row[3]}")

                if not Trip.objects.filter(trip_id='3_10494220').exists():
                    raise Exception(f"There is no trip with id {row[0]}")

                trip_id = Trip.objects.get(trip_id=row[0])
                stop_id = Stop.objects.get(id=row[3])

                # correct format in datetime row (tak, naprawdę są tam krzaczki typu godzina 25:00 lub 26:00)
                if row[1].startswith("24") or row[1].startswith("25") or row[1].startswith("26"):
                    row[1] = row[1].replace(row[1][0:2], "00", 1)

                if row[2].startswith("24") or row[2].startswith("25") or row[1].startswith("26"):
                    row[2] = row[2].replace(row[2][0:2], "00", 1)

                _, created = StopTimes.objects.get_or_create(
                    trip_id=trip_id,
                    arrival_time=row[1],
                    departure_time=row[2],
                    stop_id=stop_id,
                    stop_sequence=row[4],
                    pickup_type=row[5],
                    drop_off_time=row[6],
                )

        all_stoptimes = StopTimes.objects.all()
        print(all_stoptimes)
