from django.db import models
from django.urls import reverse
from paagrio.utils import unique_slug_generator,random_string_generator
from django.db.models.signals import pre_save, post_save
import random
import os
# Create your models here.
POST_TYPES = [
 ('news','News'),
 ('fix','Fix'),
]
LANGUAGE_TYPES = [
 ('ka','Georgian'),
 ('en','English'),
 ('ru','Russian'),
]

class News(models.Model):
    title = models.CharField(max_length=65)
    title_ka = models.CharField(max_length=65)
    title_ru = models.CharField(max_length=65)
    text = models.TextField(max_length=1024)
    text_ka = models.TextField(max_length=1024)
    text_ru = models.TextField(max_length=1024)
    type = models.CharField(max_length=10,choices=POST_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    post_language = models.CharField(max_length=255, choices=LANGUAGE_TYPES,null=True,blank=True)
    slug = models.SlugField(max_length=255,unique=True)

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

def product_pre_save_reciever(sender,instance,*args,**kwargs):
    if instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_reciever,sender=News)
