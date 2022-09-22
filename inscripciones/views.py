from django.shortcuts import render

# Create your views here.
from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import InscribirseSerializers, PrincipalSerializers, PrincipalSerializers,InscribirseSerializers
from .models import Principal, inscribirse, inscribirse, Principal
from rest_framework import status
from django.http import Http404
from django.shortcuts import render

# Create your views here.
class Principal_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=PrincipalSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class Principal_APIView_List(APIView):

    def get(self, request, format=None, *args, **kwargs):
        Princ = Principal.objects.all()
        serializer = PrincipalSerializers(Princ, many=True)
        return Response(serializer.data)


class inscripciones_APIView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer=InscribirseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class inscripciones_APIView(APIView):

    def get(self, request, format=None, *args, **kwargs):
        inscripcion = inscribirse.objects.all()
        serializer = InscribirseSerializers(inscripcion, many=True)
        return Response(serializer.data)