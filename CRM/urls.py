from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'CRM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   # url(r'^Ventas/', include('Ventas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('Ventas.urls')),

]
