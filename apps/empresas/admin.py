# apps/empresas/admin.py
from django.contrib import admin
from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['nome_fantasia', 'cnpj', 'cidade', 'estado', 'ativo', 'criado_em']
    list_filter = ['ativo', 'estado', 'modulo_vendas', 'modulo_compras']
    search_fields = ['nome', 'nome_fantasia', 'cnpj']
    readonly_fields = ['id', 'criado_em', 'atualizado_em']
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'inscricao_municipal')
        }),
        ('Contato', {
            'fields': ('telefone', 'celular', 'email', 'site')
        }),
        ('Endereço', {
            'fields': ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado')
        }),
        ('Aparência', {
            'fields': ('logo', 'cor_primaria', 'cor_secundaria')
        }),
        ('Módulos', {
            'fields': ('modulo_vendas', 'modulo_compras', 'modulo_estoque', 'modulo_financeiro')
        }),
        ('Status', {
            'fields': ('ativo', 'limite_usuarios', 'data_expiracao')
        }),
    )