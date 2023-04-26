from django.urls import path
from django.views.generic import TemplateView

from . import views

handler404 = 'eventos.views.custom_404'

urlpatterns = [
    path('', views.EventosListView.as_view(),name="index"),
    path("about/", TemplateView.as_view(template_name="about.html")),
    path('detalle/<pk>', views.detalle.as_view(),name="detalle"),
    path('contacto/', views.ContactoView.as_view(),name="contacto"),
    #path('', views.index,name="index"),
    #path('detalle/<codigo>', views.detalle),
    #path('about/', views.about),
    #path('detalle/<codigo>', views.detalle),
    #path('contacto/', views.contacto),
]