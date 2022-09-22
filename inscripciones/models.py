from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Principal(models.Model):
    apellidos=models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)
    nombres=models.CharField(max_length=100, verbose_name='Descripcion', null=True, blank=True)
    cedula=models.CharField(max_length=20, verbose_name='Cedula',null=True, blank=True)
    celular=models.CharField(max_length=10, verbose_name='Celular', null=True, blank=True)
    
    
    class Meta:
        verbose_name='principal'
        verbose_name_plural='Principales'

    def __str__(self):
        return str(self.nombres)

class inscribirse(models.Model):
    principal = models.ManyToManyField(Principal, verbose_name="Principal", blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Fotografia", upload_to="users")
    public=models.BooleanField(verbose_name="¿Enviar Formulario?")
    finscripcion = models.DateField(null=True, blank=True, verbose_name="Fecha de Inscripcion" )
    facultad = models.CharField(max_length=100, verbose_name='Escriba la facultad',null=True, blank=True)
    carrera = models.CharField(max_length=150, verbose_name='Escriba la carrera universitaria',null=True, blank=True)
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='inscribirse'
        verbose_name_plural='Inscripciones'

    def __str__(self):
        return str(self.principal)

