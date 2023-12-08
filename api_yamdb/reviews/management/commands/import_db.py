from csv import DictReader

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from reviews.models import (
    Category,
    Comment,
    Genre,
    GenreToTitle,
    Review,
    Title,
)

from api_yamdb.settings import BASE_DIR

User = get_user_model()


class Command(BaseCommand):
    help = "CSV"

    def get_user(self):
        if User.objects.exists():
            self.stdout.write("База User уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/users.csv",
            encoding="utf8",
            #  newline=''#
        )
        reader = DictReader(csvfile)
        for line in reader:
            User.objects.create(
                id=line["id"],
                username=line["username"],
                email=line["email"],
                role=line["role"],
                bio=line["bio"],
                first_name=line["first_name"],
                last_name=line["last_name"],
            )
        self.stdout.write("База User - окей!")

    def get_genre(self):
        if Genre.objects.exists():
            self.stdout.write("База Genre уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/genre.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            Genre.objects.create(
                id=line["id"],
                name=line["name"],
                slug=line["slug"],
            )
        self.stdout.write("База Genre - окей!")

    def get_category(self):
        if Category.objects.exists():
            self.stdout.write("База Category уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/category.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            Category.objects.create(
                id=line["id"],
                name=line["name"],
                slug=line["slug"],
            )
        self.stdout.write("База Category - окей!")

    def get_title(self):
        if Title.objects.exists():
            self.stdout.write("База Title уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/titles.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            Title.objects.create(
                id=line["id"],
                name=line["name"],
                year=line["year"],
                category=Category.objects.get(id=line["category"]),
            )
        self.stdout.write("База Title - окей!")

    def get_genre_to_title(self):
        if GenreToTitle.objects.exists():
            self.stdout.write("База GenreToTitle уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/genre_title.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            GenreToTitle.objects.create(
                id=line["id"],
                title_id=line["title_id"],
                genre_id=line["genre_id"],
            )
        self.stdout.write("База GenreToTitle - окей!")

    def get_review(self):
        if Review.objects.exists():
            self.stdout.write("База Review уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/review.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            Review.objects.create(
                id=line["id"],
                title_id=line["title_id"],
                text=line["text"],
                author=User.objects.get(id=line["author"]),
                score=line["score"],
                pub_date=line["pub_date"],
            )
        self.stdout.write("База Review - окей!")

    def get_comment(self):
        if Comment.objects.exists():
            self.stdout.write("База Comment уже и так непуста.")
            return
        csvfile = open(
            BASE_DIR / "static/data/comments.csv",
            encoding="utf8",
            #  newline=''
        )
        reader = DictReader(csvfile)
        for line in reader:
            Comment.objects.create(
                id=line["id"],
                review_id=line["review_id"],
                text=line["text"],
                author=User.objects.get(id=line["author"]),
                pub_date=line["pub_date"],
            )
        self.stdout.write("База Comment - окей!")

    def handle(self, *args, **kwargs):
        self.get_user()
        self.get_genre()
        self.get_category()
        self.get_title()
        self.get_genre_to_title()
        self.get_review()
        self.get_comment()
