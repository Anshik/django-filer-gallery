# -*- coding: utf-8 -*-
from django.utils import simplejson
from filer_gallery import settings as filer_gallery_settings

try:
    from django.views.generic import ListView
    from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
except ImportError:
    from cbv import ListView, ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
    
from categories.views import get_category_for_path

class ConfigMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ConfigMixin, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
        
class CategoryAllRelatedList(ListView, ConfigMixin):
    
    path_field = 'category_path'
    category_field = 'category'
    
    def get_queryset(self):
        queryset = super(CategoryAllRelatedList, self).get_queryset()
        category = get_category_for_path(self.kwargs[self.path_field])
        kwargs = {
            '%s__tree_id' % self.category_field: category.tree_id,
            '%s__lft__gte' % self.category_field: category.lft,
            '%s__rght__lte' % self.category_field: category.rght
        }
        return queryset.filter(**kwargs).order_by('%s__lft' % self.category_field)

    def get_template_names(self):
        names = []
        if hasattr(self.object_list, 'model'):
            opts = self.object_list.model._meta
            path_items = self.kwargs[self.path_field].strip('/').split('/')
            while path_items:
                names.append( '%s/category_all_%s_%s%s.html' % (opts.app_label,
                                                            '_'.join(path_items),
                                                            opts.object_name.lower(),
                                                            self.template_name_suffix)
                                                            )
                path_items.pop()
            names.append('%s/category_all_%s%s.html' % (opts.app_label,
                                                    opts.object_name.lower(),
                                                    self.template_name_suffix)
                                                    )
        names.extend(super(CategoryAllRelatedList, self).get_template_names())
        return names
        
    def get_context_data(self, **kwargs):
        context = super(CategoryAllRelatedList, self).get_context_data(**kwargs)
        context['category'] = get_category_for_path(self.kwargs['category_path'])
        return context

class ImageViaGalleryCategoryList(CategoryAllRelatedList):
    category_field = 'gallery__category'

class GalleryArchiveIndexView(ArchiveIndexView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryArchiveIndexView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
    
class GalleryYearArchiveView(YearArchiveView, ConfigMixin):
    
    make_object_list = True
    
    def get_context_data(self, **kwargs):
        context = super(GalleryYearArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
    
class GalleryMonthArchiveView(MonthArchiveView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryMonthArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
    
class GalleryDayArchiveView(DayArchiveView, ConfigMixin):
    def get_context_data(self, **kwargs):
        context = super(GalleryDayArchiveView, self).get_context_data(**kwargs)
        context['ORBIT_CONFIG'] = simplejson.dumps(filer_gallery_settings.ORBIT_CONFIG)
        context['SKITTER_CONFIG'] = simplejson.dumps(filer_gallery_settings.SKITTER_CONFIG)
        context['FILER_GALLERY_DISPLAY_SIZE'] = filer_gallery_settings.FILER_GALLERY_DISPLAY_SIZE
        return context
