from django.contrib import admin
from .models import matricula, DatosMatricula

# Register your models here.

class datosmatriculaAdmin(admin.ModelAdmin):
    readonly_fields = ('Nombre',)
    search_fields = ('Nombre','Apellido','Cedula','carrera','Semestre',)
    list_display = ('Nombre','Apellido','Cedula','carrera','Semestre',)
    ordering=('-Nombre',)

class matriculaAdmin(admin.ModelAdmin):
    readonly_fields = ('cedula',)
    search_fields = ('cedula','Nombres','Apellidos','Carrera','Semestre','fmatricula',)
    list_display = ('cedula','Nombres','Apellidos','Carrera','Semestre','fmatricula',)
    ordering=('-create_at',)

admin.site.register(DatosMatricula, datosmatriculaAdmin)
admin.site.register(matricula, matriculaAdmin)