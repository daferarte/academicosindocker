from django.urls import path
from .views import *

urlpatterns = [
    path('v1/nota/', nota_APIView.as_view()),
    path('v1/notas/', notas_APIView.as_view()),
]
