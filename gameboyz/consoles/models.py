from django.db import models

class Platform(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    slug = models.SlugField(db_index=True)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
        
