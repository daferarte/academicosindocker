from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estudiante(models.Model):
    Nombre=models.CharField(max_length=150, verbose_name='Nombres del Estudiante', null=True, blank=True)
    Apellido=models.CharField(max_length=150, verbose_name='Apellidos del Estudiante', null=True, blank=True)
    cedula=models.CharField(max_length=150, verbose_name='Cedula', null=True, blank=True)
    celular=models.CharField(max_length=100, verbose_name='Celular', null=True, blank=True)
    carrera=models.CharField(max_length=100, verbose_name='Carrera', null=True, blank=True)
    facultad=models.CharField(max_length=100, verbose_name='Facultad', null=True, blank=True)

    class Meta:
        verbose_name='Estudiante'
        verbose_name_plural='Estudiantess'

    def __str__(self):
        return str(self.Nombre)

class Estudiantess(models.Model):
    tipoDocumento = models.ManyToManyField(Estudiante, verbose_name="Estudiantes", blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    horasdesalida=models.CharField(max_length=100, verbose_name='Hora de Salida', null=True, blank=True)
    public=models.BooleanField(verbose_name="¿Publicado?")
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Estudiantess'
        verbose_name_plural='Estudiante'

    def __str__(self):
        return str(self.horasdesalida)

