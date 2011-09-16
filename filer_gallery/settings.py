from django.conf import settings

ORBIT_CONFIG = getattr(settings, 'ORBIT_CONFIG', {
    'advanceSpeed': 4000,
    'animation': 'horizontal-slide',
    'animationSpeed': 600,
    'bullets': True,
    'captionAnimation': 'none',
    'captionAnimationSpeed': 800,
    'captions': True,
    'directionalNav': False,
    'pauseOnHover': True,
    'startClockOnMouseOut': True,
    'startClockOnMouseOutAfter': 1000,
    'timer': True
})

SKITTER_CONFIG = getattr(settings, 'SKITTER_CONFIG', {
    'navigation': True,
    'interval': 2500,
    'numbers': True,
    'label': True,
    'animation': 'random',
    'thumbs': False,
    'hideTools': False,
    'dots': False,
    'easing_default': None,
    'velocity': 1,
    'animateNumberOut': {'backgroundColor':'#000', 'color':'#ccc'},
    'animateNumberOver': {'backgroundColor':'#000', 'color':'#ccc'},
    'animateNumberActive': {'backgroundColor':'#000', 'color':'#ccc'},
    'width_label': None,
    'show_randomly': False
})

FILER_GALLERY_DISPLAY_SIZE = getattr(settings, 'FILER_GALLERY_DISPLAY_SIZE', (400, 300) )
