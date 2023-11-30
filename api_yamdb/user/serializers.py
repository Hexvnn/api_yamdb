from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class UsernameValidationMixin:
    def validate_username(self, value):
        if value == "me":
            raise ValidationError(f"Логин {value} использовать нельзя")
        return value


class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField(read_only=True)
    username = serializers.SlugField(read_only=True)
    email = serializers.EmailField(read_only=True)

    class Meta:
        model = User
        exclude = ["role"]
        ordering = ["id"]


class UserCreationSerializer(
    UsernameValidationMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = User
        ordering = ["id"]
        fields = "__all__"


class SignUpSerializer(UsernameValidationMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class GetTokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "confirmation_code")
