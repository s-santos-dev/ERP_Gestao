# apps/auditoria/services.py
from .models import LogAuditoria


def registrar_auditoria(
    usuario,
    acao: str,
    app_label: str,
    model_name: str,
    objeto_id: str = '',
    descricao: str = '',
    dados_antes: dict = None,
    dados_depois: dict = None,
    ip_address: str = None,
    user_agent: str = '',
    empresa=None
) -> LogAuditoria:
    """
    Registra uma ação no log de auditoria.
    Deve ser chamado por signals ou middleware.
    """
    log = LogAuditoria.objects.create(
        usuario=usuario,
        empresa=empresa or getattr(usuario, 'empresa', None),
        acao=acao,
        app_label=app_label,
        model_name=model_name,
        objeto_id=str(objeto_id) if objeto_id else '',
        descricao=descricao,
        dados_antes=dados_antes or {},
        dados_depois=dados_depois or {},
        ip_address=ip_address,
        user_agent=user_agent
    )
    return log