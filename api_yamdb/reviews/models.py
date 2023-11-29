from django.db import models


MAX_TEXT_LENGTH = 256


class CatGenBaseModel(models.Model):
    '''Абстракт для моделей Category и Genre.'''
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_TEXT_LENGTH,
        help_text='Внести название'
    )
    slug = models.SlugField(
        verbose_name='Идентификатор',
        max_length=MAX_TEXT_LENGTH,
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
    '''Модель самих наших нетленок.
    '''
    name = models.CharField(
        verbose_name='Название',
        max_length=MAX_TEXT_LENGTH,
        help_text='Внести название'
    )
    year = models.IntegerField(
        verbose_name='Дата выпуска',
        help_text='Внести дату выпуска',
        #  validators=(validate_title_year,)
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
        #  related_name='titles',
        verbose_name='Категория',
        help_text='Внести категорию',
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

    def __str__(self):
        return f'{self.title} относится к жанру {self.genre}'
