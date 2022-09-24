from rest_framework import serializers
from .models import nota, notas

class notaSerializers(serializers.ModelSerializer):
    class Meta:
        model = nota
        fields = '__all__'

class notasSerializers(serializers.ModelSerializer):
    class Meta:
        model = notas
        field = '__all__'