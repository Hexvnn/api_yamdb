from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (CategoryViewSet,
                       GenreViewSet,
                       ReviewViewSet,
                       CommentViewSet,
                       TitleViewSet)

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register("titles", TitleViewSet, basename="titles")
router.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet,
    basename="review"
)
router.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet,
    basename="comments"
)

urlpatterns = [
    #  path("v1/auth/signup/", ...),
    #  path("v1/auth/token/", ...),
    path("v1/", include(router.urls)),
]
