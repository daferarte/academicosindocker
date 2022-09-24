from django.urls import path
from .views import *

urlpatterns = [
    path('v1/Semestre/', Semestre_APIView.as_view()),
    path('v1/Semestres/', Semestres_APIView.as_view()),
]
