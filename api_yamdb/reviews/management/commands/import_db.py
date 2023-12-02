from csv import DictReader
# https://docs-python.ru/standart-library/modul-csv-python/klass-dictreader-modulja-csv/
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from api_yamdb.settings import BASE_DIR
from reviews.models import (Category,
                            Comment,
                            Genre,
                            GenreToTitle,
                            Review,
                            Title)

User = get_user_model()


class Command(BaseCommand):
    help = 'CSV'

    def GetUser(self):
        if User.objects.exists():
            print('База User уже и так непуста.')
        else:
            # https://docs-python.ru/tutorial/vstroennye-funktsii
            # -interpretatora-python/funktsija-open/
            csvfile = open(BASE_DIR / 'static/data/users.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                User.objects.create(
                    id=line['id'],
                    username=line['username'],
                    email=line['email'],
                    role=line['role'],
                    bio=line['bio'],
                    first_name=line['first_name'],
                    last_name=line['last_name'])
            print('База User - окей!')

    def GetGenre(self):
        if Genre.objects.exists():
            print('База Genre уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/genre.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                Genre.objects.create(
                    id=line['id'],
                    name=line['name'],
                    slug=line['slug'])
            print('База Genre - окей!')

    def GetCategory(self):
        if Category.objects.exists():
            print('База Category уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/category.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                Category.objects.create(
                    id=line['id'],
                    name=line['name'],
                    slug=line['slug'])
            print('База Category - окей!')

    def GetTitle(self):
        if Title.objects.exists():
            print('База Title уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/title.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                Title.objects.create(
                    id=line['id'],
                    name=line['name'],
                    year=line['year'],
                    category=Category.objects.get(
                        id=line['category']))
            print('База Title - окей!')

    def GetGenreToTitle(self):
        if GenreToTitle.objects.exists():
            print('База GenreToTitle уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/genre_title.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                GenreToTitle.objects.create(
                    id=line['id'],
                    title_id=line['title_id'],
                    genre_id=line['genre_id'])
            print('База GenreToTitle - окей!')

    def GetReview(self):
        if Review.objects.exists():
            print('База Review уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/review.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                Review.objects.create(
                    id=line['id'],
                    title_id=line['title_id'],
                    text=line['text'],
                    author=User.objects.get(
                        id=line['author']),
                    score=line['score'],
                    pub_date=line['pub_date'])
            print('База Review - окей!')

    def GetComment(self):
        if Comment.objects.exists():
            print('База Comment уже и так непуста.')
        else:
            csvfile = open(BASE_DIR / 'static/data/comments.csv',
                           #  encoding='utf8',
                           #  newline=''
                           )
            reader = DictReader(csvfile)
            for line in reader:
                Comment.objects.create(
                    id=line['id'],
                    review_id=line['review_id'],
                    text=line['text'],
                    author=User.objects.get(
                        id=line['author']),
                    pub_date=line['pub_date'])
            print('База Comment - окей!')

    def handle(self, *args, **kwargs):
        self.GetUser()
        self.GetGenre()
        self.GetCategory()
        self.GetTitle()
        self.GetGenreToTitle()
        self.GetReview()
        self.GetComment()
