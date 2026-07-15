# apps/auditoria/admin.py
from django.contrib import admin
from .models import LogAuditoria


@admin.register(LogAuditoria)
class LogAuditoriaAdmin(admin.ModelAdmin):
    list_display = ['acao', 'model_name', 'usuario', 'empresa', 'criado_em']
    list_filter = ['acao', 'app_label', 'model_name', 'criado_em']
    search_fields = ['descricao', 'usuario__email', 'objeto_id']
    readonly_fields = [f.name for f in LogAuditoria._meta.fields]
    date_hierarchy = 'criado_em'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False