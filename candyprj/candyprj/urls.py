from http.client import ImproperConnectionState
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boardapp.urls')),
    path('user/', include('userapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
