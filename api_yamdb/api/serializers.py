from rest_framework import serializers
from reviews.models import Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    '''Класс сериализатора категорий нетленок.'''

    class Meta:
        model = Category
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    '''Класс сериализатора жанров нетленок.'''

    class Meta:
        model = Genre
        fields = '__all__'
