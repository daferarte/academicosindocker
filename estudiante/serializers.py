from rest_framework import serializers
from .models import Estudiante, Estudiantess

class EstudianteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class EstudiantessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estudiantess
        field = '__all__'