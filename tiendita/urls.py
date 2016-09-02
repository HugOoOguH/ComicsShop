from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'productos/$', views.ProductsListView.as_view(), name="productos"),
	url(r'detalle/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name="detail"),
]