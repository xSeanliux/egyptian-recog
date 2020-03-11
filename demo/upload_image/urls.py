from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('demo/', views.work),
    path('about/', views.about),
]