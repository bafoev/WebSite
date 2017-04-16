# -*- coding: utf-8 -*-
from django import forms


from blogs.models import Post, Blog
from comments.models import Comment


class FilterForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('description', u'Описание')
    ), label=u'Сортировать по', required=False)

    search = forms.CharField(max_length=255, label=u'Поиск', required=False)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog', 'title', 'content',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=user)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CreateCommentForm, self).is_valid()


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
        widgets = {
            'category': forms.SelectMultiple(attrs={'class': 'chosen-select'})
        }


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'category')
        widgets = {
            'category': forms.SelectMultiple(attrs={'class': 'chosen-select'})
        }
