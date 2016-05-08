import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = os.environ.get('SU_USERNAME')
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username,
                'admin@admin.com',
                os.environ.get('SU_PASSWORD')
            )
