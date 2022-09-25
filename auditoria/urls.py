from django.urls import path
from .views import *

urlpatterns = [
    path('a1/aud/', auditoria_APIView.as_view()),
    path('a1/aud1/', auditoria1_APIView.as_view()),
]
