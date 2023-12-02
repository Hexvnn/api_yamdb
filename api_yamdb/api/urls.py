from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import UserViewSet, SignUpView, TokenView

router = DefaultRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/auth/signup/", SignUpView.as_view(), name="signup"),
    path("v1/auth/token/", TokenView.as_view(), name="token"),
]
