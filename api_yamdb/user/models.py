from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = "user"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLE_CHOICES = (
        (USER, "user"),
        (MODERATOR, "moderator"),
        (ADMIN, "admin"),
    )
    username = models.SlugField(
        "Имя пользователя",
        max_length=150,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        "Эл. почта",
        blank=False,
        unique=True,
    )
    first_name = models.CharField(
        "Имя",
        max_length=150,
        blank=True,
    )
    last_name = models.CharField(
        "Фамилия",
        max_length=150,
        blank=True,
    )
    bio = models.TextField(
        "Биография",
        blank=True,
    )
    confirmation_code = models.CharField(
        "Код подтверждения",
        max_length=200,
    )
    role = models.CharField(
        "Роль",
        max_length=150,
        blank=False,
        choices=ROLE_CHOICES,
        default="user",
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR or self.is_admin
