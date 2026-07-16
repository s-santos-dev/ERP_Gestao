# apps/empresas/selectors.py
"""
Repository Pattern - Consultas de Empresas.
Toda consulta ao banco passa por aqui. Views NÃO fazem queries diretas.
"""

from django.db.models import QuerySet, Q
from .models import Empresa


def empresa_listar_todas() -> QuerySet[Empresa]:
    """Retorna todas as empresas ativas."""
    return Empresa.objects.filter(ativo=True)


def empresa_obter_por_id(empresa_id: str) -> Empresa | None:
    """Obtém uma empresa pelo ID (UUID)."""
    try:
        return Empresa.objects.get(id=empresa_id, ativo=True)
    except Empresa.DoesNotExist:
        return None


def empresa_obter_por_cnpj(cnpj: str) -> Empresa | None:
    """Obtém uma empresa pelo CNPJ (limpo)."""
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
    try:
        return Empresa.objects.get(cnpj=cnpj_limpo, ativo=True)
    except Empresa.DoesNotExist:
        return None


def empresa_filtrar_por_nome(nome: str) -> QuerySet[Empresa]:
    """Filtra empresas por nome (case-insensitive)."""
    return Empresa.objects.filter(
        Q(nome__icontains=nome) | Q(nome_fantasia__icontains=nome),
        ativo=True
    )