from django import forms
from django.utils.safestring import mark_safe

class UploadWidget(forms.Widget):

    class Media:
        css = {
            'all': ['%sfiler_gallery/fileuploader.css' % settings.STATIC_URL]
        }
        js = ['%sfiler_gallery/fileuploader.js' % settings.STATIC_URL]
    
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
        action: '/test/',
        params: {
            gallery_id: %i
        }
    }); 
})
</script>
<div id="%s_id">
</div>
''' % (name, self.obj.pk, name)
        return mark_safe(output)

