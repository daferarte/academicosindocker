from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Semestre(models.Model):
    Nombre=models.CharField(max_length=150, verbose_name='Nombres del Estudiante', null=True, blank=True)
    Apellido=models.CharField(max_length=150, verbose_name='Apellidos del Estudiante', null=True, blank=True)
    cedula=models.CharField(max_length=150, verbose_name='Cedula', null=True, blank=True)
    celular=models.CharField(max_length=100, verbose_name='Celular', null=True, blank=True)
    carrera=models.CharField(max_length=100, verbose_name='Carrera', null=True, blank=True)
    facultad=models.CharField(max_length=100, verbose_name='Facultad', null=True, blank=True)
    FechaIni=models.CharField(max_length=100, verbose_name='Fecha de Inicio', null=True, blank=True)
    FechaFin=models.CharField(max_length=100, verbose_name='Fecha Fin', null=True, blank=True)

    class Meta:
        verbose_name='Semestre'
        verbose_name_plural='Semestres'

    def __str__(self):
        return str(self.nombre)

class Semestres(models.Model):
    tipoDocumento = models.ManyToManyField(Semestre, verbose_name="Tipo de documento", blank=True)
    cedula=models.CharField(max_length=150, verbose_name='Cedula')
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    public=models.BooleanField(verbose_name="¿Publicado?")
    fNacimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de cumpleaños" )
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Semestres'
        verbose_name_plural='Semestre'

    def __str__(self):
        return str(self.cedula)