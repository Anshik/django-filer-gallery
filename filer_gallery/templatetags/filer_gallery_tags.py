from django import template
from filer_gallery.models import Gallery, GalleryImage
from categories.models import Category

register = template.Library()

@register.inclusion_tag('filer_gallery/gallery_months_links_snippet.html', takes_context=True)
def render_gallery_month_links(context):
    return {
        'dates': Gallery.objects.dates('pub_date', 'month'),
    }

@register.inclusion_tag('filer_gallery/galleryimage_months_links_snippet.html', takes_context=True)
def render_galleryimage_month_links(context):
    return {
        'dates': GalleryImage.objects.dates('pub_date', 'month')
    }
    
@register.inclusion_tag('filer_gallery/gallery_categories_links_snippet.html', takes_context=True)
def render_gallery_month_links(context):
    return {
        'category': context.get('category', None),
        'categories': Category.objects.all()
    }

@register.inclusion_tag('filer_gallery/galleryimage_categories_links_snippet.html', takes_context=True)
def render_galleryimage_month_links(context):
    return {
        'category': context.get('category', None),
        'categories': Category.objects.all()
    }
