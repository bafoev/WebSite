# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-username',)
