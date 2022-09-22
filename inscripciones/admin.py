from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Principal, inscribirse

# Register your models here.

class PrincipalAdmin(admin.ModelAdmin):
    readonly_fields = ('apellidos',)
    search_fields = ('apellidos',)
    list_display = ('apellidos','nombres','cedula','celular',)
    ordering=('-apellidos',)

class InscribirseAdmin(admin.ModelAdmin):
    readonly_fields = ('principal',)
    search_fields = ('principal',)
    list_display = ('finscripcion','facultad','carrera',)
    ordering=('-create_at',)

admin.site.register(Principal, PrincipalAdmin)
admin.site.register(inscribirse, InscribirseAdmin)
