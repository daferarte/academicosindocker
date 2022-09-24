from rest_framework import serializers
from .models import DatosMatricula, matricula

class DatosMatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = DatosMatricula
        fields = '__all__'

class matriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = matricula
        field = '__all__'