from uuid import uuid1

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions, filters
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import (
    UserTokenSerializer,
    UserSerializer,
    SignUpSerializer,
)
from api.permissions import IsAdmin


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        username = serializer.data["username"]
        if (
            User.objects.filter(username=username).exists()
            or User.objects.filter(email=email).exists
        ):
            return Response(status=status.HTTP_403_FORBIDDEN)
        code = str(uuid1())
        User.objects.get_or_create(
            username=username,
            email=email,
            confirmation_code=code,
        )
        send_mail(
            "Confirmation code",
            f"Используйте этот код для входа в учетную запись - {code}",
            "admin@yamdb.com",
            [email],
            fail_silently=False,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class TokenView(APIView):
    def post(self, request):
        serializer = UserTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data["username"]
        user = get_object_or_404(User, username=username)
        refresh = RefreshToken.for_user(user)
        return Response(
            {"access": str(refresh.access_token)},
            status=status.HTTP_200_OK,
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    http_method_names = (
        "get",
        "post",
        "patch",
        "delete",
    )
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ("username",)
    lookup_field = "username"
    pagination_class = PageNumberPagination

    @action(
        detail=False,
        methods=("GET", "PATCH"),
        permission_classes=(permissions.IsAuthenticated,),
    )
    def me(self, request):
        serializer = UserSerializer(
            request.user,
            data=request.data,
            partial=True,
        )
        if request.user.is_admin or request.user.is_moderator:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer.is_valid(raise_exception=True)
        serializer.save(role="user")
        return Response(serializer.data, status=status.HTTP_200_OK)
