from django.db import models

from gameboyz.consoles.models import Platform

class Theme(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

class Franchise(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(db_index=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(db_index=True, max_length=128)
    url = models.URLField()
    summary = models.TextField(null=True, blank=True)
    collections = models.ManyToManyField(Collection, blank=True)
    franchise = models.ForeignKey(Franchise,null=True, blank=True)
    popularity = models.FloatField()
    total_rating = models.FloatField(null=True, blank=True)
    total_rating_count = models.PositiveIntegerField(null=True, blank=True)
    first_release_date = models.DateTimeField()
    keywords = models.ManyToManyField(Keyword, blank=True)
    themes = models.ManyToManyField(Theme, blank=True)

    platforms = models.ManyToManyField(Platform)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class EbayListing(models.Model):
    title = models.TextField()
    game = models.ForeignKey(Game)
    country = models.TextField()
    location = models.TextField()
    url = models.URLField()
    condition = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title
        