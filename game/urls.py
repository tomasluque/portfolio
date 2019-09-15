from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game'),
    path('test', views.test, name='gametest'),
]
