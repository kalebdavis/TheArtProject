from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from products.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theartproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register_admin/$', 'adminuser.views.registerAdmin'),
    url(r'^login/$', 'adminuser.views.requestLogin'),
    url(r'^logout/$', 'adminuser.views.requestLogout'),
    url(r'^$', 'products.views.viewHomePage', name='home'),
    url(r'^admin_home/$', 'adminuser.views.viewHomePage', name='adminhome'),
    url(r'^products/$', 'products.views.listProducts', name='product_list'),
    url(r'^add_product/$', 'products.views.addProduct', name='product_create'),
    url(r'^(?P<product_id>\d+)', 'products.views.detailProduct', name='product_detail')) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
