# -*- coding: utf-8 -*-
from filer_gallery import settings as filer_gallery_settings
from django.conf.urls.defaults import *
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView

from filer_gallery.models import Gallery, GalleryImage
from filer_gallery.views import CategoryAllRelatedList, ImageViaGalleryCategoryList

import simplejson

extra_kwargs = {
    'ORBIT_CONFIG': simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG),
    'FILER_GALLERY_DISPLAY_SIZE': filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
}

image_info_dict = dict({
    'queryset': GalleryImage.objects.all(),
    'date_field': 'pub_date',
}, **extra_kwargs)

image_info_month_dict = dict({
    'queryset': GalleryImage.objects.all(),
    'date_field': 'pub_date',
    'month_format': '%m',
}, **extra_kwargs)

image_info_year_dict = dict({
    'queryset': GalleryImage.objects.all(),
    'date_field': 'pub_date',
}, **extra_kwargs)

gallery_info_dict = dict({
    'queryset': Gallery.objects.all(),
    'date_field': 'pub_date',
}, **extra_kwargs)

gallery_info_month_dict = dict({
    'queryset': Gallery.objects.all(),
    'date_field': 'pub_date',
    'month_format': '%m',
}, **extra_kwargs)

gallery_info_year_dict = dict({
    'queryset': Gallery.objects.all(),
    'date_field': 'pub_date',
}, **extra_kwargs)

urlpatterns = patterns('',

    url(r'^$',
        ArchiveIndexView.as_view(**image_info_dict),
        name= 'filer_gallery_galleryimage_archive_index'),
        
    url(r'^images/(?P<year>\d{4})/$', 
        YearArchiveView.as_view(**image_info_year_dict),
        name= 'filer_gallery_galleryimage_archive_year'),
    
    url(r'^images/(?P<year>\d{4})/(?P<month>\d{2})/$', 
        MonthArchiveView.as_view(**image_info_month_dict),
        name= 'filer_gallery_galleryimage_archive_month'),
    
    url(r'^images/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 
        DayArchiveView.as_view(**image_info_month_dict),
        name= 'filer_gallery_galleryimage_archive_day'),
        
    url(r'^images/(?P<category_path>.+)/$',
        ImageViaGalleryCategoryList.as_view(model=GalleryImage, **extra_kwargs),
        name='filer_gallery_galleryimage_gallery_category'),
        
    url(r'^images/(?P<category_path>.+)/$',
        CategoryAllRelatedList.as_view(model=GalleryImage, **extra_kwargs),
        name='filer_gallery_galleryimage_category'),
        
    url(r'^galleries/$',
        ArchiveIndexView.as_view(**gallery_info_dict),
        name= 'filer_gallery_gallery_archive_index'),
    
    url(r'^galleries/(?P<year>\d{4})/$', 
        YearArchiveView.as_view(**gallery_info_year_dict),
        name= 'filer_gallery_gallery_archive_year'),
    
    url(r'^galleries/(?P<year>\d{4})/(?P<month>\d{2})/$', 
        MonthArchiveView.as_view(**gallery_info_month_dict),
        name= 'filer_gallery_gallery_archive_month'),
    
    url(r'^galleries/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 
        DayArchiveView.as_view(**gallery_info_month_dict),
        name= 'filer_gallery_gallery_archive_day'),
        
    url(r'^galleries/(?P<category_path>.+)/$',
        CategoryAllRelatedList.as_view(model=Gallery),
        name='filer_gallery_galleryimage_category')              
)