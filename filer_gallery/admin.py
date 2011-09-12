# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms.fields import Field
from filer_gallery.models import Gallery, GalleryImage
from filer_gallery.widgets import UploadWidget

class GalleryAdmin(admin.ModelAdmin):
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(GalleryAdmin, self).get_form(request, obj=None, **kwargs)
        if obj:
            form.base_fields['upload'] = Field(widget=UploadWidget(obj=obj))
        return form

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage)
