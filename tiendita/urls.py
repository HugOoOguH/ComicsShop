from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'comic_shop/$', views.CompaniesListView.as_view(), name="companies"),
	url(r'comics_list/(?P<id>\d+)$', views.ComicsListView.as_view(), name="comics"),
	url(r'detalle/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name="detail"),
]