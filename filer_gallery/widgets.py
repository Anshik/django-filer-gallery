from django.conf import settings
from django import forms
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

class UploadWidget(forms.Widget):

    class Media:
        css = {
            'all': ['%sfiler_gallery/fileuploader/fileuploader.css' % settings.STATIC_URL]
        }
        js = ['%sfiler_gallery/fileuploader/fileuploader.js' % settings.STATIC_URL]
    
    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')        
        super(UploadWidget, self).__init__(*args, **kwargs)
            
    is_hidden = False
    
    def render(self, name, value, attrs=None):
        output = u'''
<script type="text/javascript">
django.jQuery(document).ready(function () {
    var uploader = new qq.FileUploader({
        element: document.getElementById('%s_id'),
        action: '%s',
        params: {
            gallery_id: %i
        }
    }); 
})
</script>
<div id="%s_id">
</div>
''' % (name, reverse('admin:filer_gallery_gallery_upload'), self.obj.pk, name)
        return mark_safe(output)

