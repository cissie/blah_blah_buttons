from django.conf.urls import patterns, url
from blahblahbuttons import views


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^orders$', views.shop, name='orders'),
        url(r'^cart$', views.cart, name='cart'),
        url(r'^products', views.cart, name='products'),
        url(r'^product_detail(?P<slug>[0-9A-Za-z-_.//]+)/$', views.cart, name='product_detail')
)
