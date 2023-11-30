#  from django.shortcuts import render
from rest_framework.mixins import (CreateModelMixin,
                                   DestroyModelMixin,
                                   ListModelMixin)
from rest_framework import filters, viewsets
from api.permissions import (IsAdminOrReadOnly)
from api.serializers import (CategorySerializer,
                             GenreSerializer)
from reviews.models import (Category,
                            Genre)


class CategoryViewSet(CreateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateModelMixin,
                   ListModelMixin,
                   DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
