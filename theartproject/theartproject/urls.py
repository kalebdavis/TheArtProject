from django.conf.urls import patterns, include, url

from django.contrib import admin

from products.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theartproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'products.views.viewHomePage', name='home'),
    url(r'^products/$', 'products.views.listProducts', name='product_list'),
    url(r'^add_product/$', 'products.views.addProduct', name='product_create'),
)
