# apps/core/models.py
"""
Modelos base e mixins reutilizáveis em todo o ERP.
Todo modelo do ERP deve herdar de BaseModel.
"""

from django.db import models
from django.conf import settings
import uuid


class BaseModel(models.Model):
    """
    Modelo abstrato base para TODOS os modelos do ERP.
    Fornece: id (UUID), timestamps, soft-delete, empresa e usuário.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    
    # Relacionamentos obrigatórios para multi-tenancy e auditoria
    empresa = models.ForeignKey(
        'empresas.Empresa',
        on_delete=models.CASCADE,
        related_name='%(class)s_empresa',
        verbose_name='Empresa',
        null=True, blank=True  # Permitir null temporariamente para superusuários
    )
    
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='%(class)s_criado_por',
        verbose_name='Criado por'
    )
    
    atualizado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='%(class)s_atualizado_por',
        verbose_name='Atualizado por'
    )

    class Meta:
        abstract = True
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.__class__.__name__} ({self.id})"


class EnderecoMixin(models.Model):
    """Mixin para modelos que possuem endereço."""
    cep = models.CharField(max_length=9, blank=True, verbose_name='CEP')
    logradouro = models.CharField(max_length=255, blank=True, verbose_name='Logradouro')
    numero = models.CharField(max_length=20, blank=True, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    bairro = models.CharField(max_length=100, blank=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, blank=True, verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=True, verbose_name='UF')
    
    class Meta:
        abstract = True


class ContatoMixin(models.Model):
    """Mixin para modelos que possuem contato."""
    telefone = models.CharField(max_length=20, blank=True, verbose_name='Telefone')
    celular = models.CharField(max_length=20, blank=True, verbose_name='Celular')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    site = models.URLField(blank=True, verbose_name='Website')
    
    class Meta:
        abstract = True