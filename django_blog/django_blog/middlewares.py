import logging
from django.http import HttpResponseForbidden

logger = logging.getLogger(__name__)

ALLOWED_IP = '31.155.17.5'  

class AdminIPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] != ALLOWED_IP:
            ip_address = request.META['REMOTE_ADDR']

            logger.warning(f"Erisim engellendi: {ip_address} adresi ile /admin/ sayfasina erismeye calisti.")
            return HttpResponseForbidden("Bu sayfaya erişiminiz yok.")
        return self.get_response(request)
