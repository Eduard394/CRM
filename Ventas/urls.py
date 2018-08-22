from django.conf.urls import patterns, include
from django.conf.urls import include, url

from . import views

urlpatterns = [
    #url(r'^index',name = 'index' ),
    url(r'^$', views.post_list),
]