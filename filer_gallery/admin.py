# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms.fields import Field
from django import forms
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from filer.models import Image

class UploadImageFileForm(forms.ModelForm):
    
    class Meta:
        model = Image
        
from filer import settings as filer_settings
from filer_gallery.models import Gallery, GalleryImage
from filer_gallery.widgets import UploadWidget
from filer_gallery.utils import handle_upload, UploadException

class GalleryAdmin(admin.ModelAdmin):
        
    list_display = ('__unicode__', 'title', 'show_images')
    list_editable = ('title',)
    list_filter = ('category',)
    
    prepopulated_fields = {'slug': ('title',) }
    
    def show_images(self, obj):
        return u'<a href="%s?gallery__exact=%i">Show images</a>' % (reverse('admin:filer_gallery_galleryimage_changelist'), obj.pk)
    show_images.allow_tags = True
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(GalleryAdmin, self).get_form(request, obj=None, **kwargs)
        if obj:
            form.base_fields['upload'] = Field(widget=UploadWidget(obj=obj), required=False)
        return form
        
    def get_urls(self):
        from django.conf.urls.defaults import patterns, url
        urls = super(GalleryAdmin, self).get_urls()
        url_patterns = patterns('',
            url(r'upload/$',self.ajax_upload,
                name='filer_gallery_gallery_upload'
            )
        )
        url_patterns.extend(urls)
        return url_patterns
                
    @csrf_exempt
    def ajax_upload(self, request):
        """
        receives an upload from the uploader. Receives only one file at the time.
        """
        gallery = Gallery.objects.get(pk=request.REQUEST.get("gallery_id"))
        try:
            upload, filename, is_raw = handle_upload(request)

            uploadform = UploadImageFileForm({'original_filename': filename,
                                   'owner': request.user.pk},
                                  {'file': upload})
            if uploadform.is_valid():
                file_obj = uploadform.save(commit=False)
                # Enforce the FILER_IS_PUBLIC_DEFAULT
                file_obj.is_public = filer_settings.FILER_IS_PUBLIC_DEFAULT
                file_obj.save()
                GalleryImage.objects.create(gallery=gallery, category=gallery.category, title=gallery.title, image=file_obj)
                json_response = {
                    'thumbnail': file_obj.icons['32'],
                    'alt_text': '',
                    'label': unicode(file_obj),
                    'success': True
                }
                return HttpResponse(simplejson.dumps(json_response), mimetype='application/json')
            else:
                form_errors = '; '.join(['%s: %s' % (
                    field,
                    ', '.join(errors)) for field, errors in uploadform.errors.items()
                ])
                raise UploadException("AJAX request not valid: form invalid '%s'" % (form_errors,))
        except UploadException, e:
            return HttpResponse(simplejson.dumps({'error': unicode(e)}), mimetype='application/json')
            
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'image', 'category')
    list_editable = ('title', 'image', 'category')
    list_filter = ('gallery',)
    
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
