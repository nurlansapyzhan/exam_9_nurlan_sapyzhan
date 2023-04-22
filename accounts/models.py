from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


class Account(AbstractUser):
    username = models.CharField(
        max_length=50,
        verbose_name='Username',
        null=False,
        unique=True
    )
    favorite_posts = models.ManyToManyField(
        to='app.PhotoModel',
        verbose_name='Favorite posts',
        related_name='favorite'
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
