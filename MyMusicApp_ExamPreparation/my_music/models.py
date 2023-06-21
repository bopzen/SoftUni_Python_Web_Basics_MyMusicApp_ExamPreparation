from django.db import models
from django.core import validators
from MyMusicApp_ExamPreparation.my_music.validators import validate_only_alphanumeric


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15
    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
            validate_only_alphanumeric
        ),
        null=False,
        blank=False
    )
    email = models.EmailField(
        null=False,
        blank=False
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )


class Album(models.Model):

    GENRES = [
        ('Pop Music', "Pop Music"),
        ('Jazz Music', "Jazz Music"),
        ('R&B Music', "R&B Music"),
        ('Rock Music', "Rock Music"),
        ('Country Music', "Country Music"),
        ('Dance Music', "Dance Music"),
        ('Hip Hop Music', "Hip Hop Music"),
        ('Other', "Other"),
    ]

    MAX_LEN_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        unique=True,
        max_length=MAX_LEN_NAME,
        null=False,
        blank=False,
        verbose_name='Album Name'
    )
    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        null=False,
        blank=False
    )
    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        choices=GENRES,
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )

    )



