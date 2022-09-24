from turtle import mode
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class nota(models.Model):
    nombre=models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)
    tipoDocumento=models.CharField(max_length=20, verbose_name='tipoDocumento', null=True, blank=True)
    materia=models.CharField(max_length=50, verbose_name='materia', null=True, blank=True)
    calificaciones=models.CharField(max_length=10, verbose_name='calificaciones', null=True, blank=True)
    
    class Meta:
        verbose_name='nota'
        verbose_name_plural='notas'

    def __str__(self):
        return str(self.nombre)

class notas(models.Model):
    principal = models.ManyToManyField(nota, verbose_name='principal', blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    public=models.BooleanField(verbose_name="¿Publicado?")
    notas=models.BooleanField(verbose_name='¿Si/No?')
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Notas'
        verbose_name_plural='Notas'

    def __str__(self):
        return str(self.principal)
