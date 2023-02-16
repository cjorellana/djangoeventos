from django.urls import path
from . import views

handler404 = 'eventos.views.custom_404'

urlpatterns = [    
    path('', views.index),
    path('about/', views.about),
    path('detalle/<codigo>', views.detalle),
]