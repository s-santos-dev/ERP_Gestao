# apps/usuarios/selectors.py
from django.db.models import QuerySet
from .models import Usuario


def usuario_listar_todos() -> QuerySet[Usuario]:
    """Retorna todos os usuários ativos."""
    return Usuario.objects.filter(is_active=True)


def usuario_listar_por_empresa(empresa_id: str) -> QuerySet[Usuario]:
    """Retorna usuários de uma empresa específica."""
    return Usuario.objects.filter(empresa_id=empresa_id, is_active=True)


def usuario_obter_por_id(usuario_id: str) -> Usuario | None:
    """Obtém usuário pelo ID."""
    try:
        return Usuario.objects.get(id=usuario_id, is_active=True)
    except Usuario.DoesNotExist:
        return None


def usuario_obter_por_email(email: str) -> Usuario | None:
    """Obtém usuário pelo e-mail."""
    try:
        return Usuario.objects.get(email=email)
    except Usuario.DoesNotExist:
        return None