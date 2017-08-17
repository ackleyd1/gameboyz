from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from gameboyz.core.models import TimeStampedModel

class BaseConsole(TimeStampedModel):
    """Stores information on gaming platforms."""
    name    = models.CharField(max_length=128)
    slug    = models.SlugField(db_index=True, unique=True, max_length=128, blank=True)
    image   = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseConsole, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('baseconsole-detail', args=[str(self.id)])

class Console(TimeStampedModel):
    """Stores information on Console product releases. Related to :model:`consoles.BaseConsole`"""
    baseconsole = models.ForeignKey(BaseConsole)
    name        = models.CharField(max_length=128)
    slug        = models.SlugField(db_index=True, max_length=128)
    edition     = models.CharField(max_length=32, default="Original")
    asin        = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid        = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image       = models.ImageField(null=True, blank=True)
    published   = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.baseconsole.name)
        super(Console, self).save(*args, **kwargs)

    def __str__(self):
        return self.baseconsole.name

    def get_absolute_url(self):
        return reverse('consoles:detail', args=[str(self.id)])

