from django.core.management.base import BaseCommand
from user.models import User


class Command(BaseCommand):
    help = "csv-import"

    def ImportUser(self):
        if User.objects.exists():
            print("User'ы уже ранее были загружены")

    def handle(self, *args, **kwargs):
        self.ImportUser()
