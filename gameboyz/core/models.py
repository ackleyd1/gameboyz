from django.db import models
from django.contrib.auth.models import User

# Payment level's that are associated with the user
class Level(models.Model):
    name = models.CharField(max_length=32)
    fee = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.name

# Profile model to extend the user model
class Profile(models.Model):
    user = models.OneToOneField(User)
    sales = models.PositiveIntegerField(default=0)
    level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

