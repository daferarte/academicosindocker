from rest_framework import serializers
from .models import Principal, inscribirse

class PrincipalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = '__all__'

class InscribirseSerializers(serializers.ModelSerializer):
    class Meta:
        model = inscribirse
        field = '__all__'