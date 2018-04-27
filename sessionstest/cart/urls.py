from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.cart_home, name='cart_home'),
    url(r'^add-to-cart/(?P<slug>.*)/$', views.add_to_cart, name='add_to_cart'),
    url(r'^delete/product/(?P<product_id>\d+)/$', views.delete_cart_single, name='single_delete')
]