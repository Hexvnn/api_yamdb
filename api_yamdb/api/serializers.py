# from django.shortcuts import get_object_or_404
from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Review, Title


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
    title = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Review
        fields = "__all__"

    def validate(self, attrs):
        request = self.context.get("request")
        if request.method != "POST":
            return attrs
        author = request.user
        title_id = self.context.get("view").kwargs.get("title_id")
        if Review.objects.filter(author=author, title_id=title_id).exists():
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
