from django.contrib import admin
from .models import Estudiante, Estudiantess

# Register your models here.

class EstudiantelaseAdmin(admin.ModelAdmin):
    readonly_fields = ('Nombre',)
    search_fields = ('Nombre','Apellido','cedula','celular','carrera','facultad',)
    list_display = ('Nombre','Apellido','cedula','celular','carrera','facultad',)
    ordering=('-Nombre',)

class EstudiantessAdmin(admin.ModelAdmin):
    readonly_fields = ('horasdesalida',)
    search_fields = ('horasdesalida',)
    list_display = ('horasdesalida',)
    ordering=('-create_at',)

admin.site.register(Estudiante, EstudiantelaseAdmin)
admin.site.register(Estudiantess, EstudiantessAdmin)
