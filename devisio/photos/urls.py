from django.conf.urls import patterns, url

from views import AlbumListView

urlpatterns = patterns('',
    url('^$', AlbumListView.as_view(), name='list'),
)