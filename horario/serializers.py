from rest_framework import serializers
from .models import HorarioClase, Horario

class HorarioClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = HorarioClase
        fields = '__all__'

class HorarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Horario
        field = '__all__'