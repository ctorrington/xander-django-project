"""Command to wait for the database server to be ready."""

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management import BaseCommand
from time import sleep

class Command(BaseCommand):
    """Command to wait for the database to be ready."""
    
    def handle(self, *args, **kwargs):
        """Handle commands."""
        db_up = False
        self.stdout.write('Waiting for database')
        
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(self.style.ERROR(
                    'Database unavialable. Waiting one second...'
                ))
                sleep(1)
                
        self.stdout.write(self.style.SUCCESS(
            'Database available!'
        ))
        