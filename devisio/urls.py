from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from devisio.api import api1


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='home'),

    url(r'^api/', include(api1.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
