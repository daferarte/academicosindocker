from django.contrib import admin
from .models import pago, pagomatricula

# Register your models here.

class pagomatriculaAdmin(admin.ModelAdmin):
    readonly_fields = ('Nombre',)
    search_fields = ('Nombre','Apellido','Cedula','carrera','Semestre',)
    list_display = ('Nombre','Apellido','Cedula','carrera','Semestre',)
    ordering=('-Nombre',)

class pagomatriculaAdmin(admin.ModelAdmin):
    readonly_fields = ('cedula',)
    search_fields = ('cedula','Nombres','Apellidos','Carrera','Semestre','fmatricula',)
    list_display = ('cedula','Nombres','Apellidos','Carrera','Semestre','fmatricula',)
    ordering=('-create_at',)

admin.site.register(pagomatricula, pagomatriculaAdmin )
admin.site.register(pago, pagomatriculaAdmin)