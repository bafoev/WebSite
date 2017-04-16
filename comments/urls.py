from django.conf.urls import url

from comments.views import CommentsList

urlpatterns = [
    url('^/(?P<pk>\d+)$', CommentsList.as_view(), name='comments')
]
