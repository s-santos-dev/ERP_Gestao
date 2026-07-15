# apps/usuarios/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ['email', 'nome', 'empresa', 'is_staff', 'is_active', 'ultimo_acesso']
    list_filter = ['is_staff', 'is_active', 'empresa', 'pode_vender', 'pode_comprar']
    search_fields = ['email', 'nome', 'cargo']
    readonly_fields = ['id', 'date_joined', 'ultimo_acesso', 'criado_em']
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'avatar', 'cargo', 'departamento', 'telefone')}),
        ('Empresa', {'fields': ('empresa',)}),
        ('Permissões', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions',
                'pode_vender', 'pode_comprar', 'pode_gerenciar_estoque',
                'pode_ver_financeiro', 'pode_gerenciar_usuarios'
            )
        }),
        ('Datas', {'fields': ('date_joined', 'ultimo_acesso', 'criado_em')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2', 'empresa'),
        }),
    )
    
    ordering = ['-criado_em']