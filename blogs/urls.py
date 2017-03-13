from django.conf.urls import url

from blogs.views import BlogList, BlogDetails, PostDetails

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)$', BlogDetails.as_view(), name='blog_details'),
    url(r'^posts/(?P<pk>\d+)$', PostDetails.as_view(), name='post_details'),
]