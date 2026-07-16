# apps/empresas/models.py
from django.db import models
from apps.core.models import BaseModel, EnderecoMixin, ContatoMixin
from apps.core.utils import limpar_cnpj

class Empresa(BaseModel, EnderecoMixin, ContatoMixin):
    """
    Modelo de Empresa (Tenant).
    Cada empresa é um tenant isolado. Todos os dados pertencem a uma empresa.
    """
    nome = models.CharField(max_length=255, verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=255, blank=True, verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    inscricao_estadual = models.CharField(max_length=20, blank=True, verbose_name='Inscrição Estadual')
    inscricao_municipal = models.CharField(max_length=20, blank=True, verbose_name='Inscrição Municipal')
    logo = models.ImageField(upload_to='empresas/logos/', blank=True, verbose_name='Logo')
    cor_primaria = models.CharField(max_length=7, default='#0d6efd', verbose_name='Cor Primária')
    cor_secundaria = models.CharField(max_length=7, default='#6c757d', verbose_name='Cor Secundária')
    limite_usuarios = models.PositiveIntegerField(default=5, verbose_name='Limite de Usuários')
    data_expiracao = models.DateField(null=True, blank=True, verbose_name='Data de Expiração')
    
    # Configurações de módulos
    modulo_vendas = models.BooleanField(default=True, verbose_name='Módulo Vendas')
    modulo_compras = models.BooleanField(default=True, verbose_name='Módulo Compras')
    modulo_estoque = models.BooleanField(default=True, verbose_name='Módulo Estoque')
    modulo_financeiro = models.BooleanField(default=True, verbose_name='Módulo Financeiro')

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        permissions = [
            ('gerenciar_empresa', 'Pode gerenciar configurações da empresa'),
        ]

    def __str__(self):
        return self.nome_fantasia or self.nome

    def save(self, *args, **kwargs):
        self.cnpj = limpar_cnpj(self.cnpj)
        super().save(*args, **kwargs)