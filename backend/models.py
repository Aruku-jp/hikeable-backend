from django.db import models

class Trail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    prefecture = models.CharField(null=False, max_length=9)
    latitude = models.DecimalField(null=False, max_digits=12, decimal_places=8)
    longitude = models.DecimalField(null=False, max_digits=13, decimal_places=8)
    length = models.IntegerField(null=False)
    difficulty = models.IntegerField(null=False)
    photo_url = models.CharField(max_length=2048, null=True)
    map_url = models.CharField(max_length=2048, null=True)