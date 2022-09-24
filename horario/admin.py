from django.contrib import admin
from .models import HorarioClase, Horario

# Register your models here.

class HorarioClaseAdmin(admin.ModelAdmin):
    readonly_fields = ('nombreprofesor',)
    search_fields = ('nombreprofesor',)
    list_display = ('nombreprofesor',)
    ordering=('-nombreprofesor',)

class HorarioAdmin(admin.ModelAdmin):
    readonly_fields = ('pagosporhora',)
    search_fields = ('pagosporhora',)
    list_display = ('pagosporhora',)
    ordering=('-create_at',)

admin.site.register(HorarioClase, HorarioClaseAdmin)
admin.site.register(Horario, HorarioAdmin)
