# -*- coding: utf-8 -*-
try:
    from django.views.generic import ListView
except ImportError:
    from cbv import ListView
    
from categories.views import get_category_for_path

class CategoryAllRelatedList(ListView):
    
    category_field = 'category'
    
    def get_queryset(self):
        queryset = super(CategoryAllRelatedList, self).get_queryset()
        category = get_category_for_path(self.kwargs['category_path'])
        kwargs = {
            '%s__tree_id' % self.category_field:
            '%s__lft__gte' % self.category_field: category.lft,
            '%s__rgt__lte' % self.category_field: category.rgt
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
