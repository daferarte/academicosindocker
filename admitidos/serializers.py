from rest_framework import serializers
from .models import Admitir, Admitido

class AdmitirSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admitir
        fields = '__all__'

class AdmitidoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Admitido
        field = '__all__'