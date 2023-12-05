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

    def validate(self, data):
        if data["username"] == "me":
            raise serializers.ValidationError(
                "Пользователь с таким именем "
                "не допустим. Пожалуйста "
                "выберите другое имя."
            )
        return data


class UserTokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    def validate(self, data):
        username = data["username"]
        confirmation_code = data["confirmation_code"]
        if not User.objects.filter(username=username).exists():
            raise exceptions.NotFound("Пользователь не найден.")
        elif not User.objects.filter(
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
