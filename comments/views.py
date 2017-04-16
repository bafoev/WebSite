from django.shortcuts import render

from django.views.generic import ListView

from comments.models import Comment


class CommentsList(ListView):
    model = Comment

    template_name = 'comments/comments_list.html'
