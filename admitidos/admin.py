from django.contrib import admin
from .models import Admitir, Admitido

# Register your models here.

class AdmitirAdmin(admin.ModelAdmin):
    readonly_fields = ('apellidos',)
    search_fields = ('apellidos',)
    list_display = ('apellidos','nombres','cedula','celular','facultad','carrera','pasoalsemestre',)
    ordering=('-apellidos',)

class AdmitidoAdmin(admin.ModelAdmin):
    readonly_fields = ('admitido',)
    search_fields = ('admitido',)
    list_display = ('admitido',)
    ordering=('-create_at',)

admin.site.register(Admitir, AdmitirAdmin)
admin.site.register(Admitido, AdmitidoAdmin)
