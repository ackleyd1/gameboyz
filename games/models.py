"""
Contains models for our game app:
Franchise
GameTitle
Game
GameListing
GameListingImage
"""

import uuid

from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
from django.db import DataError

from core.models import TimeStampedModel
from consoles.models import Platform

from .utils import image_path_rename, user_game_image_upload

CONDITIONS = (
    ('new', "Brand New"),
    ('Complete In Box', (
            ('cibvgood', 'Very Good'),
            ('cibgood', 'Good'),
            ('cibacceptable', 'Acceptable'),
        )
    ),
    ('Loose', (
            ('loosevgood', 'Very Good'),
            ('loosegood', 'Good'),
            ('looseacceptable', 'Acceptable'),
        )
    ),
)

def convert_condition(condition):
    if condition == "Brand New":
        return "new"
    elif condition == "Like New":
        return "cibvgood"
    elif condition == "Very Good":
        return "loosevgood"
    elif condition == "Good":
        return "loosegood"
    elif condition == "Acceptable":
        return "looseacceptable"
    else:
        raise DataError("Hmm condition: %s" % slug)

class Franchise(TimeStampedModel):
    """Model for video game franchises, used to suggest products."""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class GameTitle(TimeStampedModel):
    """Model for a video game title."""
    name = models.CharField(max_length=128)
    url = models.URLField()
    summary = models.TextField(null=True, blank=True)
    franchise = models.ForeignKey(Franchise, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Game(TimeStampedModel):
    """Model that represents a game as a unique product that was released for a specific platform or may be a special edition."""
    gametitle = models.ForeignKey(GameTitle)
    slug = models.SlugField(db_index=True, max_length=256, blank=True, unique=True)
    edition = models.CharField(max_length=32, null=True, blank=True)
    platform = models.ForeignKey(Platform)
    asin = models.CharField(max_length=32, null=True, blank=True, unique=True)
    epid = models.CharField(max_length=32, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to=image_path_rename, null=True, blank=True)

    def __str__(self):
        return self.gametitle.name

    def get_absolute_url(self):
        return reverse('games-detail', kwargs={'platform_slug': self.platform.slug, 'game_slug': self.slug})

    def get_admin_url(self):
        return reverse('gametitles:games-detail', kwargs={'gametitle_pk': self.gametitle.pk, 'game_pk': self.pk})

    def get_price(self):
        """Returns average price for the game according to game sales, if there are none return None"""
        if self.gamesale_set.count() == 0:
            return None
        sum = 0
        for sale in self.gamesale_set.all():
            sum += sale.price
        return sum / self.gamesale_set.count()

    def get_other_games(self):
        """Returns queryset of the game title's other games (another platform or special edition)"""
        return self.gametitle.game_set.all().exclude(id=self.id)

    def save(self, *args, **kwargs):
        """Override save method to update unique slug based on the other fields."""
        slug = self.platform.slug + '-' + slugify(self.gametitle.name)
        if self.edition:
            slug = slug + '-' + slugify(self.edition)
        if Game.objects.filter(slug=slug).exclude(id=self.id).exists():
            raise DataError('Game with slug %s already exists' % slug)
        self.slug = slug
        super().save(*args, **kwargs)

class GameListing(TimeStampedModel):
    """Model for a game to be listed for sale by a user."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    condition = models.CharField(choices=CONDITIONS, max_length=32)

    def __str__(self):
        return "%s - %s" % (self.game.gametitle.name, self.condition)

    def get_absolute_url(self):
        return reverse('gamelistings-detail', kwargs={'platform_slug': self.game.platform.slug, 'game_slug': self.game.slug, 'gamelisting_id': str(self.id)})

    def get_update_url(self):
        return reverse('gamelistings-update', kwargs={'platform_slug': self.game.platform.slug, 'game_slug': self.game.slug, 'gamelisting_id': str(self.id)})

    def get_delete_url(self):
        return reverse('gamelistings-delete', kwargs={'platform_slug': self.game.platform.slug, 'game_slug': self.game.slug, 'gamelisting_id': str(self.id)})



class GameListingImage(TimeStampedModel):
    """Model for users to upload images of the game they are listing for sale."""
    gamelisting = models.ForeignKey(GameListing)
    image = models.ImageField(upload_to=user_game_image_upload)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.uuid)
