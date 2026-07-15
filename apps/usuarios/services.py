# apps/usuarios/services.py
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from .models import Usuario
from .selectors import usuario_obter_por_email


def usuario_autenticar(email: str, password: str) -> Usuario | None:
    """
    Autentica um usuário pelo e-mail e senha.
    Retorna o usuário ou None se falhar.
    """
    user = authenticate(username=email, password=password)
    if user and isinstance(user, Usuario) and user.is_active:
        return user
    return None


def usuario_criar(
    email: str,
    nome: str,
    password: str,
    empresa=None,
    **kwargs
) -> Usuario:
    """
    Cria um novo usuário com validações.
    
    Regras:
    - E-mail deve ser único
    - Senha deve ter no mínimo 8 caracteres
    """
    if len(password) < 8:
        raise ValidationError('A senha deve ter no mínimo 8 caracteres.')
    
    if usuario_obter_por_email(email):
        raise ValidationError('Já existe um usuário com este e-mail.')
    
    usuario = Usuario.objects.create_user(
        email=email,
        nome=nome,
        password=password,
        empresa=empresa,
        **kwargs
    )
    
    return usuario


def usuario_atualizar_perfil(usuario: Usuario, **dados) -> Usuario:
    """Atualiza o perfil do usuário."""
    campos_permitidos = ['nome', 'cargo', 'departamento', 'telefone', 'avatar']
    
    for campo, valor in dados.items():
        if campo in campos_permitidos and hasattr(usuario, campo):
            setattr(usuario, campo, valor)
    
    usuario.save()
    return usuario