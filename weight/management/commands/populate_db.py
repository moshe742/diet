from datetime import date, datetime
import csv

from django.core.management.base import BaseCommand, CommandError

from weight.models import Weight


class Command(BaseCommand):
    help = 'populate the db from a csv'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        with open(options['file_name']) as csvfile:
            csv_data = csv.DictReader(csvfile)
            records = []
            for record in csv_data:
                record_date = datetime.strptime(record['date'], '%Y-%m-%d') if record['date'] else None
                record_new_weight = record['new_weight'] if record['new_weight'] else None
                records.append((date.today(), date.today(), record_date, record['old_weight'], record_new_weight))
                Weight.objects.create(date=record_date, old_weight=record['old_weight'], new_weight=record_new_weight)
