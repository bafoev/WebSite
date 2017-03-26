from django.views.generic import TemplateView
from blogs.models import Blog, Post, Like
from comments.models import Comment
from core.models import User


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['n_users'] = User.objects.all().count()
        context['n_blogs'] = Blog.objects.all().count()
        context['n_posts'] = Post.objects.all().count()
        context['n_comments'] = Comment.objects.all().count()
        context['n_likes'] = Like.objects.all().count()
        return context
