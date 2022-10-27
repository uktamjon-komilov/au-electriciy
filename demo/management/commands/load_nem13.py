from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Loads NEM13 type CSV files into the database"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass