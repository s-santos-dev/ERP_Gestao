# apps/usuarios/managers.py
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    """Manager customizado para o modelo Usuario."""
    
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError(_('O e-mail é obrigatório'))
        if not nome:
            raise ValueError(_('O nome é obrigatório'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superusuário deve ter is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superusuário deve ter is_superuser=True.'))

        return self.create_user(email, nome, password, **extra_fields)