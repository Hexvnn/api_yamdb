from django.db.models import Avg
from django_filters.rest_framework import (CharFilter,
                                           DjangoFilterBackend,
                                           FilterSet)
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


class TitleFilter(FilterSet):
    # https://django-filter.readthedocs.io/en/main/ref/filters.html
    # Модели для фильтров: genre, category;
    # поле: slug;
    # icontains: case-insensitive containment.
    genre = CharFilter(field_name='genre__slug', lookup_expr='icontains')
    category = CharFilter(field_name='category__slug', lookup_expr='icontains')

    class Meta:
        model = Title
        fields = '__all__'


class CategoryViewSet(CreateModelMixin,
                      ListModelMixin,
                      DestroyModelMixin,
                      viewsets.GenericViewSet):
    # Можно бы и миксины вынести и замешать где-то не здесь,
    # чтобы два раза все не перечислять.
    # Но лень.
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    # В локаторе для удаления объекта приходит
    # не 'pk', а 'slug':
    lookup_field = "slug"


class GenreViewSet(CreateModelMixin,
                   ListModelMixin,
                   DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name",)
    # В локаторе для удаления объекта приходит
    # не 'pk', а 'slug':
    lookup_field = "slug"


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.order_by('id').annotate(
        rating=Avg("reviews__score")
    )
    http_method_names = ["get", "post", "patch", "delete"]
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    # Поле фильтрации зададим в классе фильтрующего бекенда.
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return TitleReadSerializer
        return TitleWriteSerializer
