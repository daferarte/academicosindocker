from django.shortcuts import render

# Create your views here.
from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdmitirSerializers, AdmitidoSerializers
from .models import Admitido, Admitir
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class Admitir_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=AdmitirSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Admitir_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        Princ = Admitir.objects.all()
        serializer = AdmitirSerializers(Princ, many=True)
        return Response(serializer.data)


class Admitido_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=AdmitidoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Admitido_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        inscripcion = Admitido.objects.all()
        serializer = AdmitidoSerializers(inscripcion, many=True)
        return Response(serializer.data)