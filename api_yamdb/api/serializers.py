import datetime as dt

from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


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

    def to_representation(self, title):
        serializer = TitleReadSerializer(title)
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    score = serializers.IntegerField(
        min_value=1,
        max_value=10,
    )
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Review
        fields = "__all__"

    def validate(self, attrs):
        request = self.context.get("request")
        author = request.user
        title_id = self.context.get("view").kwargs.get("title_id")
        title = get_object_or_404(Title, pk=title_id)
        if (
            request.method == "POST"
            and Review.objects.filter(author=author, title=title).exists()
        ):
            raise serializers.ValidationError("Вы уже оставляли отзыв.")
        return attrs


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
