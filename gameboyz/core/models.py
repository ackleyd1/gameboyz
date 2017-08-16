from django.db import models
from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
    """Abstract model for inheriting created and updated fields."""
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Level(models.Model):
    """Stores levels of commission fees. Needs work."""
    name = models.CharField(max_length=32)
    fee = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.name

class Profile(models.Model):
    """
    Related to a single :model:`auth.User` and stores the users :model:`gameboyz.sales.Sale` and current :model:`gameboyz.core.Level`
    """
    user = models.OneToOneField(User)
    sales = models.PositiveIntegerField(default=0)
    level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

