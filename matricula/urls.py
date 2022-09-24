from django.urls import path
from .views import *

urlpatterns = [
    path('v2/DatosMatricula/', DatosMatricula_APIView.as_view()),
    path('v2/matricula/', matricula_APIView.as_view()),
]