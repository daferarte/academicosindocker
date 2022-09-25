from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import auditoria1Serializers,auditoriaSerializers
from .models import auditoria1, auditoria
from rest_framework import status
from django.http import Http404
from django.shortcuts import render
# Create your views here.

class auditoria_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=auditoriaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class auditoria_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = auditoria.objects.all()
        serializer = auditoriaSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class auditoria1_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=auditoria1Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
