from faker import Faker
from django_seed import Seed
from django.core.management.base import BaseCommand
from boards.models import Board
from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = "This command creates boards"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many boards do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = User.objects.all()
        fake = Faker(["ko_KR"])

        for user in users:
            Board.objects.create(
                author=user, title=fake.unique.bs(), content=fake.unique.bs()
            )

        self.stdout.write(self.style.SUCCESS(f"{number} boards created!"))
