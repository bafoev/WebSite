from django.views.generic import TemplateView
from blogs.models import Blog, Post, Like
from comments.models import Comment
from core.models import User
from django.urls import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import login


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


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))

    else:
        form = MyUserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('core/register.html', token)
