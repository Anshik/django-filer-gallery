from django.conf import settings

ORBIT_CONFIG = getattr(settings, 'ORBIT_CONFIG', {})
FILER_GALLERY_DISPLAY_SIZE = getattr(settings, 'FILER_GALLERY_DISPLAY_SIZE', (500, 300) )
