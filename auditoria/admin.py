from django.contrib import admin
from .models import auditoria, auditoria1

# Register your models here.

class auditoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('nombre_auditor',)
    search_fields = ('nombre_auditor','cargo_auditor','area_auditor','informe_auditor',)
    list_display = ('nombre_auditor','cargo_auditor','area_auditor','informe_auditor',)
    ordering=('-nombre_auditor',)

class auditoria1Admin(admin.ModelAdmin):
    readonly_fields = ('numero_auditorias',)
    search_fields = ('numero_auditorias',)
    list_display = ('numero_auditorias',)
    ordering=('-create_at',)

admin.site.register(auditoria, auditoriaAdmin)
admin.site.register(auditoria1, auditoria1Admin)