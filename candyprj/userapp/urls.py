from django.urls import path
from . import views

app_name = 'userapp'
urlpatterns = [
     path('signup/', views.signup, name='signup'),
]