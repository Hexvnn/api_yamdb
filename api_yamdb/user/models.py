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
    bio = models.TextField("Биография", blank=True, null=True)
    role = models.CharField(
        "Роль",
        choices=ROLE_CHOICES,
        max_length=10,
        default=USER,
    )

    class Meta:
        ordering = ["id"]

    @property
    def is_admin(self):
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR or self.is_admin
