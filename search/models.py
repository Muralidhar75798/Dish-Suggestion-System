# models.py in search application
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = models.TextField()
    lat_long = models.CharField(max_length=255)
    full_details = models.TextField()
    aggregate_rating=models.DecimalField(default=0.0, max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name
