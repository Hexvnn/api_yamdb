from rest_framework import serializers
from reviews.models import Category, Genre, Title
import datetime as dt
from django.core.exceptions import ValidationError


def validate_title_year(value):
    '''Валидирует год. Что он не позже текущего.'''
    year = dt.date.today().year
    if not (value <= year):
        raise ValidationError('Некоректный год.')
    return value


class CategorySerializer(serializers.ModelSerializer):
    '''Класс сериализатора категорий нетленок.'''

    class Meta:
        model = Category
        fields = ("name",
                  "slug")


class GenreSerializer(serializers.ModelSerializer):
    '''Класс сериализатора жанров нетленок.'''

    class Meta:
        model = Genre
        fields = ("name",
                  "slug")


class TitleReadSerializer(serializers.ModelSerializer):
    '''Класс сериализатора безопасных методов с нетленками.'''
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(
        read_only=True,
        many=True
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = "__all__"
        model = Title


class TitleWriteSerializer(serializers.ModelSerializer):
    '''Класс сериализатора опасных методов с нетленками.'''
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field="slug"
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="slug",
        many=True
    )

    class Meta:
        fields = "__all__"
        model = Title

    def validate_year(self, value):
        return validate_title_year(value)
