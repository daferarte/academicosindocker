from rest_framework import serializers
from .models import auditoria, auditoria1

class auditoriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = auditoria
        fields = '__all__'

class auditoria1Serializers(serializers.ModelSerializer):
    class Meta:
        model = auditoria1
        field = '__all__'