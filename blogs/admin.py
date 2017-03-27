# -*- coding: utf-8 -*-
from django.contrib import admin
from blogs.models import Post, Blog, Category, Like

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Like)

