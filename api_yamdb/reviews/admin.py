# login/pass admin1/admin1 (temporary by Дмитрий)
from django.contrib import admin
from reviews.models import Category, Genre, GenreToTitle, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(GenreToTitle)
class GenreToTitleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'genre')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    search_fields = ('name',
                     'year',
                     'description',
                     'genre',
                     'category'
                     )
