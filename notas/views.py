from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import notaSerializers,notasSerializers
from .models import nota, notas
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class nota_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=notaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class notas_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        tpdocumento = nota.objects.all()
        serializer = notaSerializers(tpdocumento, many=True)
        return Response(serializer.data)


class notas_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=notasSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)