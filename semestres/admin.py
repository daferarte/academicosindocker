from django.contrib import admin
from .models import Semestre, Semestres

# Register your models here.

class SemestreAdmin(admin.ModelAdmin):
    readonly_fields = ('Nombre',)
    search_fields = ('Nombre','Apellido','cedula','celular','carrera','facultad',)
    list_display = ('Nombre','Apellido','cedula','celular','carrera','facultad',)
    ordering=('-Nombre',)

class SemestresAdmin(admin.ModelAdmin):
    readonly_fields = ('horasdesalida',)
    search_fields = ('horasdesalida',)
    list_display = ('horasdesalida',)
    ordering=('-create_at',)

admin.site.register(Semestre, SemestreAdmin)
admin.site.register(Semestres, SemestresAdmin)
