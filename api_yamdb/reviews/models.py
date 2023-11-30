from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


MAX_TEXT_LENGTH = 256
MAX_SLUG_LENGTH = 50


def validate_for_year(value):
    '''Проверяет год создания.'''
    #  https://docs.djangoproject.com/en/4.2/ref/validators/
    #  Поскольку валидатор на данный момент всего один, то
    #  пока не буду его выносить в отдельный файл.
    #  Если их станет не один - тогда вынесу.
    if value > timezone.now().year:
        raise ValidationError(
            (f'{value} - некорректный!'),
            params={'value': value},
        )


class CatGenBaseModel(models.Model):
    '''Абстракт для моделей Category и Genre.'''
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_TEXT_LENGTH,
        help_text='Внести название'
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=MAX_SLUG_LENGTH,
        help_text='Внести идентификатор',
        unique=True
    )

    class Meta:
        abstract = True,
        ordering = ('name',
                    'slug')

    def __str__(self):
        return self.name


class Category(CatGenBaseModel):
    '''Модель категорий наших нетленок.'''

    class Meta(CatGenBaseModel.Meta):
        verbose_name = 'объект категории'
        verbose_name_plural = 'Категории'


class Genre(CatGenBaseModel):
    '''Модель жанров наших нетленок.'''

    class Meta(CatGenBaseModel.Meta):
        verbose_name = 'объект жанра'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    '''Модель самих наших нетленок.'''
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_TEXT_LENGTH,
        help_text='Внести название'
    )
    year = models.IntegerField(
        verbose_name='Дата выпуска',
        help_text='Внести дату выпуска',
        validators=[validate_for_year]
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание',
        help_text='Внести описание',
    )
    genre = models.ManyToManyField(
        Genre,
        through='GenreToTitle',
        verbose_name='Жанр',
        help_text='Внести жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        help_text='Внести категорию',
    )
    rating = models.PositiveIntegerField(
        #  Думаю, есть два варианта с рейтингом:
        #  - хранить ср. рейтинг произведения в объекте самого произведения;
        #  - хранить рейтинг каждого отзыва и на лету считать средний.
        verbose_name='Рейтинг',
        null=True,
        default=None
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreToTitle(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Название',
        help_text='Внести название',
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
        help_text='Внести жанр',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'связь медиа с жанром'
        verbose_name_plural = 'Связи медиа с жанрами'

    def __str__(self):
        return f'{self.title} относится к жанру {self.genre}'
