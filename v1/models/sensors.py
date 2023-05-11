from django.db import models
from v1.models.geo import  District


class SensorData(models.Model):
    sensor_id = models.BigIntegerField()
    name = models.CharField(max_length=128)
    value = models.SmallIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

