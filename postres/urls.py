from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('colecciones/', views.colecciones, name='colecciones'),
    path('top/', views.top, name='top'),
]
