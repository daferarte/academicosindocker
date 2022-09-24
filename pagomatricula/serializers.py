from rest_framework import serializers
from .models import pagomatricula, pago

class pagomatriculaSerializers(serializers.ModelSerializer):
    class Meta:
        model = pagomatricula
        fields = '__all__'

class pagoSerializers(serializers.ModelSerializer):
    class Meta:
        model = pago
        field = '__all__'