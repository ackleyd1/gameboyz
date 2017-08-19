from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

from gameboyz.core.models import TimeStampedModel

class BaseConsole(TimeStampedModel):
    """Stores information on gaming platforms."""
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, unique=True, max_length=128, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseConsole, self).save(*args, **kwargs)

class Console(TimeStampedModel):
    """Stores information on Console product releases. Related to :model:`consoles.BaseConsole`"""
    baseconsole = models.ForeignKey(BaseConsole)
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, max_length=128)
    edition = models.CharField(max_length=32, default="Original")
    asin = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image = models.ImageField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.baseconsole.name) + '-' + slugify(self.edition)
        super(Console, self).save(*args, **kwargs)

    def __str__(self):
        return self.baseconsole.name

class ConsoleListing(TimeStampedModel):
    user = models.ForeignKey(User)
    console = models.ForeignKey(Console)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=32)

    def __str__(self):
        return "%s-%s" %(self.console.baseconsole.name, self.condition)


