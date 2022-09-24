from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DatosMatricula(models.Model):
    Nombre=models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)    
    Apellido=models.CharField(max_length=150, verbose_name='Apellido', null=True, blank=True)    
    Cedula=models.CharField(max_length=150, verbose_name='Cedula', null=True, blank=True)    
    carrera=models.CharField(max_length=150, verbose_name='Carrera', null=True, blank=True)    
    Semestre=models.CharField(max_length=150, verbose_name='Semestre', null=True, blank=True)
    
     
    class Meta:
        verbose_name='Matricula'
        verbose_name_plural='Mtriculas'

    def __str__(self):
        return str(self.Nombre)

class matricula(models.Model):
    tipoDocumentos = models.ManyToManyField(DatosMatricula, verbose_name="Tipo de documento", blank=True)
    cedula=models.CharField(max_length=150, verbose_name='Cedula')
    Nombres=models.CharField(max_length=150, verbose_name='Nombres')
    Apellidos=models.CharField(max_length=150, verbose_name='Apellidos')   
    Carrera=models.CharField(max_length=150, verbose_name='Carrera') 
    Semestre=models.CharField(max_length=150, verbose_name='Semestre')
    fmatricula = models.DateField(null=True, blank=True, verbose_name="Fecha de Matricula" )
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='matricul'
        verbose_name_plural='matriculas'

    def __str__(self):
        return str(self.cedula)

