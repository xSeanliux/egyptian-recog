from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('work/', views.work),
    path('about/', views.about),
    path('contact/', views.contact),
]