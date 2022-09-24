from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HorarioClaseSerializers,HorarioSerializers
from .models import HorarioClase, Horario
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class HorarioClase_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=HorarioClaseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class HorarioClase_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = HorarioClase.objects.all()
        serializer = HorarioClaseSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class Horario_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=HorarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Horario_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = Horario.objects.all()
        serializer = HorarioSerializers(tpdocumento, many=True)
        return Response(serializer.data)