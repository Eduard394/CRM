from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [
    # Examples:
    # url(r'^$', 'CRM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   # url(r'^Ventas/', include('Ventas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Ventas.urls')),
    url(r'^',login,  {'template_name':'login.html'}, name='logins'),


]
