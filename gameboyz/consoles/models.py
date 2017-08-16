from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Base Console Model (aka a platform)
class BaseConsole(models.Model):
    name    = models.CharField(max_length=128)
    slug    = models.SlugField(db_index=True, unique=True, max_length=128)
    image   = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)

pre_save.connect(slug_pre_save_receiver, sender=BaseConsole)

# Console Model