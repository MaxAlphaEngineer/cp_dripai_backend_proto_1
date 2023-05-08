from django.db import models
from v1.models.geo import Region


class SensorData(models.Model):
    sensor_id = models.BigIntegerField()
    name = models.CharField(max_length=128)
    value = models.SmallIntegerField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

