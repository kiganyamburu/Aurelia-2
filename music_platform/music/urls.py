from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('playlist/<int:id>/', views.playlist_detail, name='playlist_detail'),
]
