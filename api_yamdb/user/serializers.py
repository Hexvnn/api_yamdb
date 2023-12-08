from rest_framework import exceptions, serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )

    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError(
                "Пользователь с таким именем "
                "не допустим. Пожалуйста "
                "выберите другое имя."
            )
        return value


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        username = data["username"]
        confirmation_code = data["confirmation_code"]
        if not User.objects.filter(username=username).exists():
            raise exceptions.NotFound("Пользователь не найден.")
        if not User.objects.filter(
            confirmation_code=confirmation_code,
        ).exists():
            raise serializers.ValidationError("Неправильный код")
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
