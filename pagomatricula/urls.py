from django.urls import path
from .views import *

urlpatterns = [
    path('v2/DatosMatricula/', pagomatricula_APIView.as_view()),
    path('v2/matricula/', pago_APIView.as_view()),
]