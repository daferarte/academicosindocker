from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ContratoSerializers,DocenteSerializers
from .models import Docente, Contrato
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class Docente_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=DocenteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Docente_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = Docente.objects.all()
        serializer = DocenteSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class Contrato_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=ContratoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Contrato_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = Contrato.objects.all()
        serializer = ContratoSerializers(tpdocumento, many=True)
        return Response(serializer.data)