from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class DefaultVerboseNameMadel(models.Model):
    """Абстрактная модель. Установка related_name."""
    class Meta:
        abstract = True
        default_related_name = '%(class)ss'


class Review(models.Model):

    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=512)
    score = models.PositiveSmallIntegerField(max=10)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta(DefaultVerboseNameMadel):
        ordering = ["-pub_date"]
