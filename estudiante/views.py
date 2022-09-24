from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EstudianteSerializers,EstudiantessSerializers
from .models import Estudiante, Estudiantess
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class Estudiante_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=EstudianteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Estudiante_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = Estudiante.objects.all()
        serializer = EstudianteSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class Estudiantess_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=EstudiantessSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Estudiantess_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = Estudiantess.objects.all()
        serializer = EstudiantessSerializers(tpdocumento, many=True)
        return Response(serializer.data)