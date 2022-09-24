from django.urls import path
from .views import *

urlpatterns = [
    path('v3/Estudiante/', Estudiante_APIView.as_view()),
    path('v3/Estudiantess/', Estudiantess_APIView.as_view()),
]
