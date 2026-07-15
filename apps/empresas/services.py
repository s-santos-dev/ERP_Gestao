# apps/empresas/services.py
"""
Service Layer - Regras de Negócio de Empresas.
Toda lógica de negócio fica aqui. Views chamam services, não tocam models.
"""

from django.core.exceptions import ValidationError
from .models import Empresa
from .selectors import empresa_obter_por_cnpj


def empresa_criar(
    nome: str,
    cnpj: str,
    nome_fantasia: str = '',
    **kwargs
) -> Empresa:
    """
    Cria uma nova empresa com validações de negócio.
    
    Regras:
    - CNPJ deve ser único
    - CNPJ deve ter 14 dígitos
    """
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
    
    if len(cnpj_limpo) != 14:
        raise ValidationError('CNPJ deve conter 14 dígitos.')
    
    if empresa_obter_por_cnpj(cnpj_limpo):
        raise ValidationError('Já existe uma empresa com este CNPJ.')
    
    empresa = Empresa.objects.create(
        nome=nome,
        cnpj=cnpj_limpo,
        nome_fantasia=nome_fantasia,
        **kwargs
    )
    
    return empresa


def empresa_atualizar(empresa: Empresa, **dados) -> Empresa:
    """Atualiza dados de uma empresa com validações."""
    if 'cnpj' in dados:
        cnpj_novo = ''.join(filter(str.isdigit, dados['cnpj']))
        if cnpj_novo != empresa.cnpj and empresa_obter_por_cnpj(cnpj_novo):
            raise ValidationError('CNPJ já está em uso por outra empresa.')
        dados['cnpj'] = cnpj_novo
    
    for campo, valor in dados.items():
        if hasattr(empresa, campo):
            setattr(empresa, campo, valor)
    
    empresa.save()
    return empresa


def empresa_desativar(empresa: Empresa) -> None:
    """Soft-delete: desativa a empresa em vez de apagar."""
    empresa.ativo = False
    empresa.save()