from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from products.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'theartproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^register_admin/$', 'adminuser.views.registerAdmin'),
    url(r'^login/$', 'adminuser.views.requestLogin'),
    url(r'^logout/$', 'adminuser.views.requestLogout'),

    url(r'^$', 'products.views.viewHomePage', name='home'),
    url(r'^admin_home/$', 'adminuser.views.viewHomePage', name='adminhome'),

    url(r'^products/$', 'products.views.listProducts', name='product_list'),
    url(r'^products/(?P<product_id>\d+)', 'products.views.filteredProducts', name='product_list_filtered'),
    url(r'^add_product/$', 'products.views.addProduct', name='product_create'),
    url(r'^delete_product/$', 'products.views.viewProductsToDelete', name='product_create'),
    url(r'^delete/(?P<product_id>\d+)/$', 'products.views.deleteProduct', name='product_delete'),
    url(r'^(?P<product_id>\d+)', 'products.views.detailProduct', name='product_detail'),

    #url(r'^contact/$', 'products.views.about', name='about'),
    #url(r'^contact/$', 'products.views.about', name='contact'),
    url(r'^payment/$', TemplateView.as_view(template_name="payment.html")),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html")),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html')),
    url(r'^submit/$', 'products.views.submitProduct', name='submit_product'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)