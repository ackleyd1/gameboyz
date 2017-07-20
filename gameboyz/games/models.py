from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from .managers import ThemeManager, KeywordManager, FranchiseManager, CollectionManager, BaseGameManager
# Most of these models serve simply as a way of classifying games for suggesting to users

class Theme(models.Model):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)
    igdb = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)

    # time information
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    # set the manager for the model
    objects = ThemeManager()

    def __str__(self):
        return self.name

class Keyword(models.Model):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)
    igdb = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)

    # time information
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    # set the manager for the model
    objects = KeywordManager()

    def __str__(self):
        return self.name

class Franchise(models.Model):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)
    igdb = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)

    # time information
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    # set the manager for the model
    objects = FranchiseManager()

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)
    igdb = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)

    # time information
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    # set the manager for the model
    objects = CollectionManager()

    def __str__(self):
        return self.name

class BaseGame(models.Model):
    # Always has this info, slug is automatically generated
    name                = models.CharField(max_length=128)
    slug                = models.SlugField(db_index=True, unique=True, max_length=128)
    url                 = models.URLField()
    popularity          = models.FloatField()

    # Some instances have these, images will be added in later
    first_release_date  = models.DateTimeField(null=True, blank=True)
    image               = models.ImageField(null=True, blank=True)
    summary             = models.TextField(null=True, blank=True)
    total_rating        = models.FloatField(null=True, blank=True)
    total_rating_count  = models.PositiveIntegerField(null=True, blank=True)

    # relationships each instance will have
    franchise           = models.ForeignKey(Franchise,null=True, blank=True)
    collections         = models.ManyToManyField(Collection, blank=True)
    keywords            = models.ManyToManyField(Keyword, blank=True)
    themes              = models.ManyToManyField(Theme, blank=True)
    consoles            = models.ManyToManyField("consoles.BaseConsole")

    # ids for igdb.com, pricecharting.com, amazon.com, ebay.com
    igdb                = models.PositiveIntegerField(db_index=True, null=True, blank=True, unique=True)
    pcid                = models.PositiveIntegerField(null=True, blank=True, unique=True)
    asin                = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid                = models.CharField(max_length=32, null=True, blank=True, unique=True)

    # time information
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    # set the manager for the model
    objects = BaseGameManager()

    def __str__(self):
        return self.name

def create_slug(instance, sender, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, sender, new_slug=new_slug)
    return slug
        
# uses django's slugify to create the slug from the title before the model is saved
def slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = create_slug(instance, sender)

# connects to all models here so far
pre_save.connect(slug_pre_save_receiver, sender=Theme)
pre_save.connect(slug_pre_save_receiver, sender=Keyword)
pre_save.connect(slug_pre_save_receiver, sender=Franchise)
pre_save.connect(slug_pre_save_receiver, sender=Collection)
pre_save.connect(slug_pre_save_receiver, sender=BaseGame)

