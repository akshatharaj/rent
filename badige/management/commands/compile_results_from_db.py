import json
from django.core.management.base import BaseCommand, CommandError
from badige.compile_data import compile_best_marketing_roi

class Command(BaseCommand):
    help = 'identify the best marketing source, by dollar spent per lead cost. Please provide <YYYY> <quarter> as args' 

    def handle(self, *args, **options):
        if not int(options['year']) in range(2000, 2015) or not int(options['quarter']) in range(1, 5):
            raise CommandError('Please provide valid year (2010-2015) and quarter (1-4)')
        compile_best_marketing_roi(int(options['quarter']), int(options['year']))

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('year', type=int)
        parser.add_argument('quarter', type=int)
