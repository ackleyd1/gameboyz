"""
Contains models for our consoles app:
Platform
Console
ConsoleListing
"""

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from core.models import TimeStampedModel

class Platform(TimeStampedModel):
    """Model for a gaming Platform."""
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, unique=True, max_length=128, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('overview', kwargs={'platform_slug': self.slug})

class Console(TimeStampedModel):
    """Model for a Console that was supports a specific platform."""
    platform = models.ForeignKey(Platform)
    slug = models.SlugField(db_index=True, max_length=128)
    edition = models.CharField(max_length=32, default="Original")
    asin = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.platform.name) + '-' + slugify(self.edition)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.platform.name + self.edition

class ConsoleListing(TimeStampedModel):
    """Model for a Console to be listed for sale by a user."""
    user = models.ForeignKey(User)
    console = models.ForeignKey(Console)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=32)

    def __str__(self):
        return "%s - %s" %(self.console.__str__(), self.condition)


