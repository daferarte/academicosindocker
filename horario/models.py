from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HorarioClase(models.Model):
    nombreprofesor=models.CharField(max_length=150, verbose_name='Nombre Profesor', null=True, blank=True)
    materia=models.CharField(max_length=150, verbose_name='Materia', null=True, blank=True)
    numerohoras=models.CharField(max_length=100, verbose_name='Numero de Horas', null=True, blank=True)
    diaclases=models.CharField(max_length=100, verbose_name='Día de clases', null=True, blank=True)
    
    class Meta:
        verbose_name='HorariodeClase'
        verbose_name_plural='Horarios de Clases'

    def __str__(self):
        return str(self.nombreprofesor)

class Horario(models.Model):
    tipoDocumento = models.ManyToManyField(HorarioClase, verbose_name="Horarios de Clase", blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    pagosporhora=models.CharField(max_length=150, verbose_name='Materia', null=True, blank=True)
    public=models.BooleanField(verbose_name="¿Publicado?")
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Horario'
        verbose_name_plural='Horarios'

    def __str__(self):
        return str(self.pagosporhora)

