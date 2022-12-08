from django.db import models


class Trail (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, null=False, max_length=255)
    prefecture = models.CharField(null=False, max_length=9)
    latitude = models.DecimalField(null=False, max_digits=12, decimal_places=8)
    longitude = models.DecimalField(
        null=False, max_digits=13, decimal_places=8)
    length = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    difficulty = models.IntegerField(null=False)
    photo_url = models.CharField(max_length=2048, blank=True)
    map_url = models.CharField(max_length=2048, blank=True)


class TrailComment (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("Account", on_delete=models.CASCADE)
    trail_id = models.ForeignKey("Trail", on_delete=models.CASCADE)
    comment = models.TextField(max_length=10000, blank=False)
    date = models.DateField(null=False)


class Account (models.Model):
    id = models.AutoField(primary_key=True)
    firebase_uid = models.CharField(max_length=128, unique=True)


class TrailLike (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("Account", on_delete=models.CASCADE)
    trail_id = models.ForeignKey("Trail", on_delete=models.CASCADE)
    like = models.BooleanField(null=False)


class TrailCompletion (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("Account", on_delete=models.CASCADE)
    trail_id = models.ForeignKey("Trail", on_delete=models.CASCADE)
    completion = models.BooleanField(null=False)
    date = models.DateField(null=False)


def __str__(self):
    return self.user.username
