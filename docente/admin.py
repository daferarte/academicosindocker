from django.contrib import admin
from .models import Contrato, Docente

# Register your models here.

class DocenteAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre',)
    search_fields = ('nombre','identificacionprofe','carrera','asignatura',)
    list_display = ('nombre','identificacionprofe','carrera','asignatura',)
    ordering=('-nombre',)

class ContratoAdmin(admin.ModelAdmin):
    readonly_fields = ('tipoContrato',)
    search_fields = ('tipoContrato','tecnico','tecnicoen','tecnologo','tecnologoen','profesional','profesionalen','posgrado','posgradoen',)
    list_display = ('tipoContrato','tecnico','tecnicoen','tecnologo','tecnologoen','profesional','profesionalen','posgrado','posgradoen',)
    ordering=('-create_at',)

admin.site.register(Docente, DocenteAdmin)
admin.site.register(Contrato, ContratoAdmin)