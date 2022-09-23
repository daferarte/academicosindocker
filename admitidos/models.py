from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admitir(models.Model):
    apellidos=models.CharField(max_length=150, verbose_name='Apellidos', null=True, blank=True)
    nombres=models.CharField(max_length=100, verbose_name='Nombres', null=True, blank=True)
    cedula=models.CharField(max_length=20, verbose_name='Cedula',null=True, blank=True)
    celular=models.CharField(max_length=10, verbose_name='Celular', null=True, blank=True)
    facultad=models.CharField(max_length=100, verbose_name='Facultad', null=True, blank=True)
    carrera=models.CharField(max_length=100, verbose_name='Carrera', null=True, blank=True)
    pasoalsemestre=models.CharField(max_length=100, verbose_name='Semestre Pasado', null=True, blank=True)
        
    class Meta:
        verbose_name='Admitir'
        verbose_name_plural='Admitidos'

    def __str__(self):
        return str(self.apellidos)

class Admitido(models.Model):
    principal = models.ManyToManyField(Admitir, verbose_name="Principal", blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Fotografia", upload_to="users")
    public=models.BooleanField(verbose_name="¿Enviar Formulario?")
    admitido=models.BooleanField(verbose_name="¿Si/No?")
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Admitido'
        verbose_name_plural='Admitidos'

    def __str__(self):
        return str(self.principal)

