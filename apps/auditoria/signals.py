# apps/auditoria/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .services import registrar_auditoria
import threading
from .services import registrar_auditoria
 
_thread_locals = threading.local()
 
 
def get_current_user_and_request():
    return (
        getattr(_thread_locals, 'usuario', None),
        getattr(_thread_locals, 'ip_address', None),
        getattr(_thread_locals, 'user_agent', ''),
    )
 
 
@receiver(post_save)
def auditoria_post_save(sender, instance, created, **kwargs):
    """Registra criação e atualização de qualquer modelo."""
    if sender._meta.app_label in ['auditoria', 'admin', 'contenttypes', 'sessions']:
        return
 
    usuario, ip, agent = get_current_user_and_request()
    registrar_auditoria(
        usuario=usuario,
        acao='CRIAR' if created else 'ATUALIZAR',
        app_label=sender._meta.app_label,
        model_name=sender._meta.model_name,
        objeto_id=str(instance.pk),
        descricao=str(instance),
        ip_address=ip,
        user_agent=agent,
    )

@receiver(post_save)
def auditoria_post_save(sender, instance, created, **kwargs):
    """Registra criação e atualização de qualquer modelo."""
    # Ignorar modelos do próprio app de auditoria e do admin
    if sender._meta.app_label in ['auditoria', 'admin', 'contenttypes', 'sessions']:
        return
    
    from django.contrib.auth import get_user_model
    Usuario = get_user_model()
    
    # Tentar obter usuário da thread (via middleware ou signal)
    # Simplificado: não registra se não houver usuário no contexto
    pass  # Será implementado com middleware de thread local


@receiver(post_delete)
def auditoria_post_delete(sender, instance, **kwargs):
    """Registra deleção de qualquer modelo."""
    if sender._meta.app_label in ['auditoria', 'admin', 'contenttypes', 'sessions']:
        return
    pass