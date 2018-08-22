from django.conf.urls import patterns, include
from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^index',name = 'index' ),
    url(r'^$', views.client_list),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
]