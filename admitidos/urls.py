from django.urls import path
from .views import *

urlpatterns = [
    path('v1/Admitir/', Admitir_APIView.as_view()),
    path('v1/Admitido/', Admitido_APIView.as_view()),
]
