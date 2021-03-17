from django.contrib import admin
from django.urls import path
from webapp import views



urlpatterns = [
    path('', views.home, name="Home"),
    path('estadistica', views.estadistica, name="Estadistica"),
    path('pronostico', views.pronostico, name="Pronostico"),
    path('contacto', views.contacto, name="Contacto"),
    path("machine-learning/<int:x>",views.machineLearning,name="naiveBayes"),# Cambiale despues que funcione
]
