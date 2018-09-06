from django.conf.urls import patterns, include
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.auth.decorators import login_required
from Ventas.views import Cliente_list, Cliente_create,Producto_list,Producto_create
from . import views

urlpatterns = [
    #url(r'^index',name = 'index' ),
   # url(r'^',login,  {'template_name':'login_tim.html'}, name='logins'),
    #url(r'^$', views.index),
    url(r'^inicio', login_required(views.home), name = 'inicio' ),
    url(r'^client/listar', views.client_list,name='clintsList'),
    #url(r'^client/new/$', views.client_new, name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.client_detail, name='client_detail'),
    #url(r'^client/(?P<pk>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    #url(r'^producto/list', views.producto_list,name='producto_list'),
    #url(r'^producto/new/$', views.producto_new, name='producto_new'),
    url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
    #url(r'^producto/(?P<pk>[0-9]+)/edit/$', views.producto_edit, name='producto_edit'),
    #url(r'^venta/new/$', views.venta_new, name='venta_new'),
    #url(r'^venta/list', views.venta_list,name='venta_list'),
    url(r'^venta/(?P<pk>[0-9]+)/$', views.venta_detail, name='venta_detail'),
    url(r'^venta/(?P<pk>[0-9]+)/edit/$', views.venta_edit, name='venta_edit'),
    #url(r'^listar', views.ListaCliente,name='ListaCliente'),
    #url(r'^all',login_required(ListaCliente.as_view()), name = 'allactivities' ),

    ### URLS con vistas Basadas en clases
    url(r'^client/list_class', Cliente_list.as_view(), name='client_listar'),
    url(r'^client/new/$', Cliente_create.as_view(), name='client_new'),
    url(r'^client/(?P<pk>[0-9]+)/edit/$', views.Cliente_edit.as_view(), name='client_edit'),
    url(r'^client/(?P<pk>[0-9]+)/delete/$', views.Cliente_delete.as_view(), name='client_delete'),

    url(r'^producto/list_class', views.Producto_list.as_view(),name='producto_listar'),
    url(r'^producto/new/$', views.Producto_create.as_view(), name='producto_new'),
    url(r'^producto/(?P<pk>[0-9]+)/edit/$', views.Producto_edit.as_view(), name='producto_edit'),
    url(r'^producto/(?P<pk>[0-9]+)/delete/$', views.Producto_delete.as_view(), name='producto_delete'),

    url(r'^venta/list', views.Venta_list.as_view(),name='venta_list'),
    url(r'^venta/new/$', views.Venta_create.as_view(), name='venta_new'),
]