# # -*- coding: utf-8 -*-
# from django import forms
# # from django.core.exceptions import PermissionDenied
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import resolve_url, get_object_or_404
# from django.views.generic import DetailView, CreateView, UpdateView
# from django.views.generic import ListView
#
# from blogs.forms import CreatePostForm, CreateCommentForm, FilterForm, UpdateBlogForm, CreateBlogForm, UpdatePostForm
# from blogs.models import Blog, Post
# from comments.models import Comment
#
#
# class SortForm(forms.Form):
#     sort = forms.ChoiceField(choices=(
#         ('title', u'заголовок'),
#         ('description', u'описание')))
#     search = forms.CharField(required=False)
#
#
# class BlogList(ListView):
#     template_name = 'blogs/blog_list.html'
#     model = Blog
#
#     sorting_form = None
#
#     def dispatch(self, request, *args, **kwargs):
#         self.sorting_form = SortForm(request.GET)
#         return super(BlogList, self).dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(BlogList, self).get_context_data(**kwargs)
#         context['sortform'] = self.sorting_form
#         return context
#
#     def get_queryset(self):
#         qs = super(BlogList, self).get_queryset()
#         if self.sorting_form.is_valid():
#             qs = qs.order_by(self.sorting_form.cleaned_data['sort'])
#             if self.sorting_form.cleaned_data['search']:
#                 qs = qs.filter(title__icontains=self.sorting_form.cleaned_data['search'])
#         return qs
#
#
# class CreateBlog(LoginRequiredMixin, CreateView):
#     model = Blog
#     fields = ('title', 'description', 'category')
#
#     template_name = 'blogs/create_blog.html'
#
#     def get_success_url(self):
#         return resolve_url('blogs:blog_details', pk=self.object.pk)
#
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super(CreateBlog, self).form_valid(form)
#
#
# class UpdateBlog(LoginRequiredMixin, UpdateView):
#     model = Blog
#     fields = ('title', 'description', 'category')
#
#     template_name = 'blogs/update_blog.html'
#
#     def get_queryset(self):
#         return Blog.objects.filter(owner=self.request.user)
#
#     def get_success_url(self):
#         return resolve_url('blogs:blog_details', pk=self.object.pk)
#
#
# class BlogDetails(DetailView):
#     template_name = 'blogs/blog_details.html'
#     model = Blog
#
#
# class PostDetails(CreateView):
#     model = Comment
#     template_name = 'blogs/post_details.html'
#     fields = ('title', 'text',)
#
#     postobject = None
#
#     def dispatch(self, request, pk=None, *args, **kwargs):
#         self.postobject = get_object_or_404(Post, id=pk)
#         return super(PostDetails, self).dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super(PostDetails, self).get_context_data(**kwargs)
#         context['post'] = self.postobject
#         return context
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.post = self.postobject
#         return super(PostDetails, self).form_valid(form)
#
#     def get_success_url(self):
#         return resolve_url('blogs:post_details', pk=self.postobject.pk)
#
#
# class CreatePost(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ('blog', 'title', 'content',)
#
#     template_name = 'blogs/create_post.html'
#
#     def get_success_url(self):
#         return resolve_url('blogs:post_details', pk=self.object.pk)
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super(CreatePost, self).form_valid(form)
#
#
# class UpdatePost(LoginRequiredMixin, UpdateView):
#     model = Post
#     fields = ('title', 'content',)
#
#     template_name = 'blogs/update_post.html'
#
#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)
#
#     def get_success_url(self):
#         return resolve_url('blogs:post_details', pk=self.object.pk)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView
from django.views.generic import ListView
from fm.views import AjaxCreateView, AjaxUpdateView

from blogs.forms import CreatePostForm, CreateCommentForm, FilterForm, UpdateBlogForm, CreateBlogForm, UpdatePostForm
from blogs.models import Blog, Post


class BlogList(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    filter_form = None

    def dispatch(self, request, *args, **kwargs):
        self.filter_form = FilterForm(request.GET)
        return super(BlogList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['filter_form'] = self.filter_form
        return context

    def get_queryset(self):
        qs = Blog.objects.all()
        if self.filter_form.is_valid():
            if self.filter_form.cleaned_data.get('sort'):
                qs = qs.order_by(self.filter_form.cleaned_data['sort'])
            qs = qs.filter(title__contains=self.filter_form.cleaned_data['search'])
        return qs


class CreateBlog(LoginRequiredMixin, AjaxCreateView):
    form_class = CreateBlogForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateBlog, self).form_valid(form)


class UpdateBlog(LoginRequiredMixin, AjaxUpdateView):
    form_class = UpdateBlogForm

    def get_queryset(self):
        return Blog.objects.filter(owner=self.request.user)


class BlogDetails(DetailView):
    template_name = 'blogs/blog_details.html'
    model = Blog


class PostDetails(CreateView):
    form_class = CreateCommentForm
    template_name = 'blogs/post_details.html'

    postobject = None

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            raise PermissionDenied()
        return super(PostDetails).post(request, *args, **kwargs)

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.postobject = get_object_or_404(Post, id=pk)
        return super(PostDetails, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostDetails, self).get_context_data(**kwargs)
        context['post'] = self.postobject
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.postobject
        return super(PostDetails, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('blogs:post_details', pk=self.postobject.pk)


class CreatePost(LoginRequiredMixin, AjaxCreateView):
    form_class = CreatePostForm

    def get_form_kwargs(self):
        kwargs = super(CreatePost, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, AjaxUpdateView):
    form_class = UpdatePostForm

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
