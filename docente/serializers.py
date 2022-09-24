from rest_framework import serializers
from .models import Docente, Contrato

class DocenteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class ContratoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        field = '__all__'