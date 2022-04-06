from django.core.management.base import BaseCommand
from public_transport.management.commands import import_stops, import_stop_times, import_trips

class Command(BaseCommand):
    help = 'Imports all data into database'

    def handle(self, *args, **kwargs):
        import_trips.Command.handle()
        import_stops.Command.handle()
        import_stop_times.Command.handle()
