from django.conf.urls import patterns, include
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    #url(r'^index',name = 'index' ),
   # url(r'^',login,  {'template_name':'login_tim.html'}, name='logins'),
    #url(r'^$', views.index),
    url(r'^inicio', login_required(views.home), name = 'inicio' ),
    url(r'^client/list', views.client_list),
    url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^producto/list', views.producto_list),
    url(r'^producto/new/$', views.producto_new, name='producto_new'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
    url(r'^producto/(?P<pk>[0-9]+)/edit/$', views.producto_edit, name='producto_edit'),
    url(r'^venta/new/$', views.venta_new, name='venta_new'),
    url(r'^venta/list', views.venta_list),
    url(r'^venta/(?P<pk>[0-9]+)/$', views.venta_detail, name='venta_detail'),
    url(r'^venta/(?P<pk>[0-9]+)/edit/$', views.venta_edit, name='venta_edit'),
    #url(r'^listar', views.ListaCliente,name='ListaCliente'),
    #url(r'^all',login_required(ListaCliente.as_view()), name = 'allactivities' ),
]