from django.conf.urls import url,include
from django.contrib import admin
# from accounts import urls as accountsUrls
from tiendita import urls as tiendaUrls
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    # url(r'^accounts/', include(accountsUrls)),
    url(r'^admin/', admin.site.urls),
    url(r'^tienda', include(tiendaUrls, namespace="tienda")),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),

]
