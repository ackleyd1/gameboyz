from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

from gameboyz.core.models import TimeStampedModel

from .utils import image_path_rename

class Keyword(TimeStampedModel):
    name = models.TextField()    

    def __str__(self):
        return self.name

class Franchise(TimeStampedModel):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)

    def __str__(self):
        return self.name

class Collection(TimeStampedModel):
    name = models.TextField()
    slug = models.SlugField(db_index=True, unique=True, max_length=128)

    def __str__(self):
        return self.name

class BaseGame(TimeStampedModel):
    name                = models.CharField(max_length=128)
    url                 = models.URLField()
    popularity          = models.FloatField()
    summary             = models.TextField(null=True, blank=True)
    total_rating        = models.FloatField(null=True, blank=True)
    total_rating_count  = models.PositiveIntegerField(null=True, blank=True)

    # relationships each instance will have
    franchise           = models.ForeignKey(Franchise, null=True, blank=True, on_delete=models.SET_NULL)
    collections         = models.ManyToManyField(Collection, blank=True)
    keywords            = models.ManyToManyField(Keyword, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('basegame-detail', args=[str(self.id)])

class Game(TimeStampedModel):
    basegame    = models.ForeignKey(BaseGame)
    slug        = models.SlugField(db_index=True, max_length=128)
    edition     = models.CharField(max_length=32, default="Original")
    console     = models.ForeignKey("consoles.BaseConsole")
    asin        = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid        = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image       = models.ImageField(upload_to=image_path_rename, null=True, blank=True)
    published   = models.BooleanField(default=False)

    def __str__(self):
        return self.basegame.name

    def get_absolute_url(self):
        return reverse('games:detail', args=[str(self.id)])

    def get_price(self):
        if self.gamesale_set.count() == 0:
            return None
        else:
            price = 0
            for sale in self.gamesale_set.all():
                price += sale.price
            return price / self.gamesale_set.count()

    def get_other_games(self):
        return self.basegame.game_set.all().exclude(id=self.id)

class GameListing(TimeStampedModel):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    condition = models.CharField(max_length=32)

    def __str__(self):
        return "%s-%s" %(self.game.basegame.name, self.condition)

    def get_absolute_url(self):
        return reverse('games:listing', args=[str(self.game.id), str(self.id)])


def create_unique_slug(instance, sender, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = sender.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_unique_slug(instance, sender, new_slug=new_slug)
    return slug
        
# uses django's slugify to create a unique slug from the name before the model is saved
def unique_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = create_unique_slug(instance, sender)

# same thing but doesnt use the create_unique_slug function
def game_slug_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.basegame.name:
        new_slug = slugify(instance.basegame.name)
        if sender.objects.filter(slug=new_slug, console=instance.console).exists():
            new_slug = new_slug + '-' + slugify(instance.edition)
        instance.slug = new_slug


# connects to all models here so far
pre_save.connect(unique_slug_pre_save_receiver, sender=Keyword)
pre_save.connect(unique_slug_pre_save_receiver, sender=Franchise)
pre_save.connect(unique_slug_pre_save_receiver, sender=Collection)
pre_save.connect(game_slug_pre_save_receiver, sender=Game)

