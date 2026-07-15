# apps/auditoria/models.py
from django.db import models
from django.conf import settings
import uuid


class LogAuditoria(models.Model):
    """
    Registro de todas as ações no sistema.
    Quem fez, o que fez, quando fez, em qual empresa.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='logs_auditoria'
    )
    empresa = models.ForeignKey(
        'empresas.Empresa',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='logs_auditoria'
    )
    
    # Ação realizada
    ACAO_CHOICES = [
        ('CRIAR', 'Criar'),
        ('ATUALIZAR', 'Atualizar'),
        ('DELETAR', 'Deletar'),
        ('LOGIN', 'Login'),
        ('LOGOUT', 'Logout'),
        ('EXPORTAR', 'Exportar'),
        ('IMPORTAR', 'Importar'),
        ('OUTRO', 'Outro'),
    ]
    acao = models.CharField(max_length=20, choices=ACAO_CHOICES)
    
    # Alvo da ação
    app_label = models.CharField(max_length=100, verbose_name='App')
    model_name = models.CharField(max_length=100, verbose_name='Modelo')
    objeto_id = models.CharField(max_length=100, blank=True, verbose_name='ID do Objeto')
    descricao = models.TextField(verbose_name='Descrição')
    
    # Dados extras (JSON)
    dados_antes = models.JSONField(default=dict, blank=True, verbose_name='Dados Antes')
    dados_depois = models.JSONField(default=dict, blank=True, verbose_name='Dados Depois')
    
    # Metadados da requisição
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Log de Auditoria'
        verbose_name_plural = 'Logs de Auditoria'
        ordering = ['-criado_em']
        indexes = [
            models.Index(fields=['empresa', '-criado_em']),
            models.Index(fields=['usuario', '-criado_em']),
            models.Index(fields=['acao', '-criado_em']),
        ]

    def __str__(self):
        return f"{self.acao} - {self.model_name} ({self.criado_em})"