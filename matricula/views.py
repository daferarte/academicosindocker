from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DatosMatriculaSerializers, matriculaSerializers
from .models import DatosMatricula, matricula
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class DatosMatricula_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=DatosMatriculaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class DatosMatricula_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = DatosMatricula.objects.all()
        serializer = DatosMatriculaSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class matricula_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=matriculaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
