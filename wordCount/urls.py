from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='words'),
    path('count/', views.count, name='count')
]
