from django.urls import path
from .views import *

urlpatterns = [
    path('v2/Docente/', Docente_APIView.as_view()),
    path('v2/Contrato/', Contrato_APIView.as_view()),
]
