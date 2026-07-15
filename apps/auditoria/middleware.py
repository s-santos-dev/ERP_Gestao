# apps/auditoria/middleware.py
from .services import registrar_auditoria


class AuditoriaMiddleware:
    """Middleware que captura IP e User-Agent para auditoria."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Adiciona IP e User-Agent na request para uso em views/signals
        request.ip_address = self._get_client_ip(request)
        request.user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        response = self.get_response(request)
        return response
    
    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')