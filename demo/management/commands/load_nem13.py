from django.core.management.base import BaseCommand, CommandError
from demo.utils import extract_values, create_record_from_values


class Command(BaseCommand):
    help = "Loads NEM13 type CSV files into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)

    def handle(self, *args, **options):
        path: str = options["csv_path"]

        self.stdout.write(self.style.NOTICE("Started extracting values..."))
        data: List[dict] = extract_values(path)
        self.stdout.write(self.style.SUCCESS("Finished extracting!"))

        self.stdout.write(self.style.SUCCESS("Creating database records..."))
        for item in data:
            create_record_from_values(item)

        self.stdout.write(self.style.SUCCESS("Successfully populated the database with values from the CSV file - '{}'".format(path)))