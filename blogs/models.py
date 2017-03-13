# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('-created_at',)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog')

    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)