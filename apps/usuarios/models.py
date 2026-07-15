# apps/usuarios/models.py
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel
from .managers import UsuarioManager


class Usuario(AbstractBaseUser, PermissionsMixin, BaseModel):
    """
    Modelo customizado de usuário.
    Herda de BaseModel para ter UUID, timestamps, empresa e auditoria.
    """
    email = models.EmailField(_('endereço de e-mail'), unique=True)
    nome = models.CharField(_('nome completo'), max_length=255)
    avatar = models.ImageField(upload_to='usuarios/avatars/', blank=True)
    
    # Campos de controle
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('ativo'), default=True)
    is_superuser = models.BooleanField(_('superusuário'), default=False)
    date_joined = models.DateTimeField(_('data de cadastro'), default=timezone.now)
    ultimo_acesso = models.DateTimeField(_('último acesso'), null=True, blank=True)
    
    # Campos de perfil
    cargo = models.CharField(max_length=100, blank=True, verbose_name='Cargo')
    departamento = models.CharField(max_length=100, blank=True, verbose_name='Departamento')
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    
    # Permissões por módulo (além do Django groups/permissions)
    pode_vender = models.BooleanField(default=False, verbose_name='Pode Vender')
    pode_comprar = models.BooleanField(default=False, verbose_name='Pode Comprar')
    pode_gerenciar_estoque = models.BooleanField(default=False, verbose_name='Pode Gerenciar Estoque')
    pode_ver_financeiro = models.BooleanField(default=False, verbose_name='Pode Ver Financeiro')
    pode_gerenciar_usuarios = models.BooleanField(default=False, verbose_name='Pode Gerenciar Usuários')

    # USERNAME_FIELD define qual campo é usado para login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UsuarioManager()

    class Meta:
        verbose_name = _('usuário')
        verbose_name_plural = _('usuários')
        permissions = [
            ('acessar_dashboard', 'Pode acessar o dashboard'),
            ('gerenciar_todas_empresas', 'Pode gerenciar todas as empresas (superadmin)'),
        ]

    def __str__(self):
        return self.nome or self.email

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome.split()[0] if self.nome else self.email

    def atualizar_ultimo_acesso(self):
        self.ultimo_acesso = timezone.now()
        self.save(update_fields=['ultimo_acesso'])