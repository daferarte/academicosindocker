from rest_framework import serializers
from .models import Semestre, Semestres
class SemestreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'

class SemestresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Semestres
        field = '__all__'