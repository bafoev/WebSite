from django.views.generic import DetailView
from django.views.generic import ListView

from blogs.models import Blog, Post


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog


class BlogDetails(DetailView):
    template_name = 'blogs/blog_details.html'
    model = Blog


class PostDetails(DetailView):
    template_name = 'blogs/post_details.html'
    model = Post
