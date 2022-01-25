from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('boardapp.urls')),
    path('user/', include('userapp.urls')),
]