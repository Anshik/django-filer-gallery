# -*- coding: utf-8 -*-
from django.db import models
from filer.fields.image import FilerImageField

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey('categories.Category')
    
class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey('categories.Category')
    image = FilerImageField()