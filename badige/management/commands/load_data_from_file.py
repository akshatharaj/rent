import json
from django.core.management.base import BaseCommand, CommandError
from badige import load_data
from badige.exceptions import DataLoadError

class Command(BaseCommand):
    help = 'Load json data from file at given location'

    def handle(self, *args, **options):
        try:
            # if the user provided more than one file_paths, we ignore all but first
            data = json.load(open(options['file_path']))
        except IOError:
            raise CommandError('File not found at path %s' % options['file_path'])
        except ValueError:
            raise CommandError('Invalid json data in file at %s' % options['file_path'])

        # things look good. lets try loading data
        try:
            load_data.load_data_from_json(data)
            self.stdout.write('Successfully loaded data into database')
        except DataLoadError as dle:
           self.stdout.write('Failed to load data into database %s' % str(dle))

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('file_path', type=str)


