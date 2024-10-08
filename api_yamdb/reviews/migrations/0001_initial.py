# Generated by Django 3.2 on 2023-12-08 10:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import reviews.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Внести название', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Внести идентификатор', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект категории',
                'verbose_name_plural': 'Категории',
                'ordering': ('-id', 'name', 'slug'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=256, verbose_name='Комментарий')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Добавляется автоматически', verbose_name='Дата пупликации')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-pub_date'],
                'abstract': False,
                'default_related_name': '%(class)ss',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Внести название', max_length=256, verbose_name='Название')),
                ('slug', models.SlugField(help_text='Внести идентификатор', unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'объект жанра',
                'verbose_name_plural': 'Жанры',
                'ordering': ('-id', 'name', 'slug'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenreToTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'связь медиа с жанром',
                'verbose_name_plural': 'Связи медиа с жанрами',
                'ordering': ('title', 'genre'),
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2048, verbose_name='Текст отзыва')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)], verbose_name='Оценка')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Добавляется автоматически', verbose_name='Дата пупликации')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-pub_date'],
                'abstract': False,
                'default_related_name': '%(class)ss',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Внести название', max_length=256, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(help_text='Внести дату выпуска', validators=[reviews.models.validate_for_year], verbose_name='Дата выпуска')),
                ('description', models.TextField(blank=True, help_text='Внести описание', null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(help_text='Внести категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(help_text='Внести жанр', through='reviews.GenreToTitle', to='reviews.Genre', verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
                'ordering': ('id',),
            },
        ),
    ]
