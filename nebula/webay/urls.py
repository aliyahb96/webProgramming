from django.urls import path
from . import views

app_name='webay'
urlpatterns = [
path('', views.index, name='index'),
path('profile/', views.profile, name='profile'),
]
