from django.urls import path
from .views import *

urlpatterns = [
    path('v4/HorarioClase/', HorarioClase_APIView.as_view()),
    path('v4/Horario/', Horario_APIView.as_view()),
]
