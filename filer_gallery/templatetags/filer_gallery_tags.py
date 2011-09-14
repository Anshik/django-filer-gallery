from django import template
from filer_gallery.models import Gallery, GalleryImage

register = template.Library()

@register.inclusion_tag('filer_gallery/gallery_month_links_snippet.html', takes_context=True)
def render_gallery_month_links(context):
    return {
        'dates': Gallery.objects.dates('pub_date', 'month'),
    }

@register.inclusion_tag('filer_gallery/galleryimage_months_links_snippet.html', takes_context=True)
def render_galleryimage_month_links(context):
    return {
        'dates': GalleryImage.objects.dates('pub_date', 'month')
    }