# apps/core/utils.py (novo arquivo utilitário)
def limpar_cnpj(cnpj: str) -> str:
    """Remove pontuação e valida os 14 dígitos do CNPJ."""
    cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj_limpo) != 14:
        raise ValueError('CNPJ deve conter 14 dígitos.')
    return cnpj_limpo