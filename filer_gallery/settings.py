from django.conf import settings

ORBIT_CONFIG = getattr(settings, 'ORBIT_CONFIG', {
    'advanceSpeed': 4000,
    'animation': 'horizontal-slide',
    'animationSpeed': 600,
    'bullets': False,
    'captionAnimation': 'none',
    'captionAnimationSpeed': 800,
    'captions': False,
    'directionalNav': False,
    'pauseOnHover': True,
    'startClockOnMouseOut': True,
    'startClockOnMouseOutAfter': 1000,
    'timer': True
})

FILER_GALLERY_DISPLAY_SIZE = getattr(settings, 'FILER_GALLERY_DISPLAY_SIZE', (500, 300) )
