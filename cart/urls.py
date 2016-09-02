from django.conf.urls import url
from . import views
urlpatterns=[
	url(r'^$',views.ProductDetail.as_view(), name="cart_detail"),
	url(r'^add/(?P<product_id>\d+)/$', views.Agregar.as_view(), name="cart_add"),
	url(r'^remove/(?P<product_id>\d+)/$', views.Remove.as_view(), name="cart_remove"),
]