from django.db import models
from v1.models.geo import  District


class SensorData(models.Model):
    sensor_id = models.BigIntegerField()
    name = models.CharField(max_length=128)
    tuproq_nam1 = models.JSONField()
    tuproq_nam2 = models.JSONField()
    havo_nam = models.JSONField()
    havo_temp = models.JSONField()
