from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class auditoria(models.Model):
    nombre_auditor=models.CharField(max_length=150, verbose_name='Nombre del auditor', null=True, blank=True)
    cargo_auditor=models.CharField(max_length=100, verbose_name='Cargo del auditor', null=True, blank=True)
    area_auditor=models.CharField(max_length=100, verbose_name='Area a auditar', null=True, blank=True)
    informe_auditor=models.CharField(max_length=100, verbose_name='Informe del auditor', null=True, blank=True)

    class Meta:
        verbose_name='Auditoria'
        verbose_name_plural='Auditorias'

    def __str__(self):
        return str(self.nombre_auditor)

class auditoria1(models.Model):
    tipoDocumento = models.ManyToManyField(auditoria, verbose_name="Tipo de documento", blank=True)
    numero_auditorias=models.CharField(max_length=150, verbose_name='Cedula')
    user=models.OneToOneField(User,  verbose_name="Usuario", on_delete=models.CASCADE) #clave relacional del modelo de usuarios de django
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="users")
    public=models.BooleanField(verbose_name="¿Publicado?")
    create_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Editado')    

    class Meta:
        verbose_name='auditoria1'
        verbose_name_plural='auditorias1'

    def __str__(self):
        return str(self.numero_auditorias)
    