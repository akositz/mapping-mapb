from django.db import models

# Create your models here.
class Points(models.Model):
    point_name = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()