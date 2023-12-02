# login/pass admin1/admin1 (temporary by Дмитрий)
from django.contrib import admin
from reviews.models import Category, Genre, GenreToTitle, Title, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(GenreToTitle)
class GenreToTitleAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'genre'
                    )
    search_fields = ('title', 'genre')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'year',
                    'description',
                    'category'
                    )
    search_fields = ('name',
                     'year',
                     'description',
                     'genre',
                     'category'
                     )
