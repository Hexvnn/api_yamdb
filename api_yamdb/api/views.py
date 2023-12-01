from django.db.models import Avg
#  from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import (CreateModelMixin,
                                   DestroyModelMixin,
                                   ListModelMixin)
from rest_framework import filters, viewsets
from api.permissions import (IsAdminOrReadOnly)
from api.serializers import (CategorySerializer,
                             GenreSerializer,
                             TitleReadSerializer,
                             TitleWriteSerializer,
                             )
from reviews.models import (Category,
                            Genre,
                            Title)


class CategoryViewSet(CreateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class GenreViewSet(CreateModelMixin,
                   ListModelMixin,
                   DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')
    ).all()
    permission_classes = (IsAdminOrReadOnly,)
    #  filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleReadSerializer
        return TitleWriteSerializer
