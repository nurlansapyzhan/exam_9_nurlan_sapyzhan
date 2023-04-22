from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class PhotoModel(models.Model):
    photo = models.ImageField(
        null=False,
        blank=True,
        upload_to='photos',
        verbose_name='Фотография'
    )
    description = models.CharField(
        max_length=200,
        verbose_name='Подпись фотограции',
        null=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата-время создания'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='photos',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        default=1
    )

