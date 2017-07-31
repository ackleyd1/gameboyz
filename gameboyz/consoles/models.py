from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .managers import BaseConsoleManager

class BaseConsole(models.Model):
    name    = models.CharField(max_length=128)
    slug    = models.SlugField(db_index=True, unique=True, max_length=128)
    image   = models.ImageField(null=True, blank=True)
    igdb    = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)
    objects = BaseConsoleManager()

    def __str__(self):
        return self.name

    def google(self):
        return self.name.replace(' ', '+')

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)

pre_save.connect(slug_pre_save_receiver, sender=BaseConsole)


        
