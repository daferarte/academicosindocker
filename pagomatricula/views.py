from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import pagomatriculaSerializers, pagoSerializers
from .models import pagomatricula, pago
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class pagomatricula_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=pagomatriculaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class pagomatricula_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = pagomatricula.objects.all()
        serializer = pagomatriculaSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class pago_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=pagoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
