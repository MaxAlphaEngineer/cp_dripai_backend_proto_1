from django.db import models


class SensorData(models.Model):
    sensor_id = models.BigIntegerField()
    name = models.CharField(max_length=128)
    value = models.SmallIntegerField()

