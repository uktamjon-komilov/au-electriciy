from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Loads NEM13 type CSV files into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str)

    def handle(self, *args, **options):
        csv_path = options["csv_path"]
        import csv;
        lst=[*csv.DictReader(open(csv_path))]
        from pprint import pprint
        print(lst)
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))