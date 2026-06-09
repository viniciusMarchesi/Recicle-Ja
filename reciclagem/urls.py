from django.urls import path
from . import views

app_name = 'reciclagem'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/pontos/', views.api_pontos_coleta, name='api_pontos_coleta'),
    path('enviar-feedback/', views.enviar_feedback, name='enviar_feedback'),
]
