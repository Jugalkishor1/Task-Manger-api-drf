from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()

        name = os.environ.get('DJANGO_SUPERUSER_NAME', 'Jugal Patel')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'Admin@1234')

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(name=name, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Superuser '{email}' created."))
        else:
            self.stdout.write(self.style.WARNING(f"Superuser '{email}' already exists."))
