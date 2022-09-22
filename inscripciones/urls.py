from django.urls import path
from .views import *

urlpatterns = [
    path('v2/principal/', Principal_APIView.as_view()),
    path('v2/inscripciones/', inscripciones_APIView.as_view()),
]
