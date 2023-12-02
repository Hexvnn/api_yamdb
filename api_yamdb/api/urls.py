from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (CategoryViewSet,
                       GenreViewSet,
                       TitleViewSet,
                       )

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("genres", GenreViewSet, basename="genres")
router.register("titles", TitleViewSet, basename="titles")

urlpatterns = [
    #  path("v1/auth/signup/", ...),
    #  path("v1/auth/token/", ...),
    path('v1/auth/', include('djoser.urls')),  # !!!!!!!!!!!!!Это только для отладки части кода!!! потом удалить!!!
    path('v1/auth/', include('djoser.urls.jwt')),  # !!!!!!!!!!!!!Это только для отладки части кода!!! потом удалить!!!
    # login/pass admin1/admin1
    # token access "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMTQ0OTY3LCJqdGkiOiI3ZmQwYThmYzZjNzg0MmIyYmM0YmM4MjJkZmZiNDEzOSIsInVzZXJfaWQiOjF9.Omga2Iawm19W9IiF1aLiT2EuInvQ93Gr-W2H7VEh1Qg"
    path("v1/", include(router.urls)),
]
