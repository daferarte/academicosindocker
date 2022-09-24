from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Docente(models.Model):
    nombre=models.CharField(max_length=150, verbose_name='Nombre', null=True, blank=True)
    identificacionprofe=models.CharField(max_length=150, verbose_name='Numero de Identificacion del Profesor', null=True, blank=True)
    carrera=models.CharField(max_length=100, verbose_name='descripcion', null=True, blank=True)
    asignatura=models.CharField(max_length=100, verbose_name='descripcion', null=True, blank=True)
    
    class Meta:
        verbose_name='Docente'
        verbose_name_plural='Docentes'

    def __str__(self):
        return str(self.nombre)

class Contrato(models.Model):
    tipoDocumento = models.ManyToManyField(Docente, verbose_name="Tipo de documento", blank=True)
    tipoContrato=models.CharField(max_length=150, verbose_name='Tipo de Contrato', null=True, blank=True)
    tecnico=models.BooleanField(verbose_name="Si/No")
    tecnicoen=models.CharField(max_length=150, verbose_name='Tecnico en: ', null=True, blank=True)
    tecnologo=models.BooleanField(verbose_name="Si/No")
    tecnologoen=models.CharField(max_length=150, verbose_name='Tecnologo en: ', null=True, blank=True)
    profesional=models.BooleanField(verbose_name="Si/No")
    profesionalen=models.CharField(max_length=150, verbose_name='Profesional en: ', null=True, blank=True)
    posgrado=models.BooleanField(verbose_name='¿Tiene algun doctorado, maestria, o otro tipo de especialidad? Si/No')
    posgradoen=models.CharField(max_length=150, verbose_name='Doctorado, Maestria o otro tipo de especialidad, escriba aqui...', null=True, blank=True)
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    public=models.BooleanField(verbose_name="¿Publicado?")
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='Contrato'
        verbose_name_plural='Contratos'

    def __str__(self):
        return str(self.tipoContrato)
