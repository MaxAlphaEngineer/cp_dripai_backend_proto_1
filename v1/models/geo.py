from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=128)

    def __str__(self):
        return self.region


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.CharField(max_length=128)

    def __str__(self):
        return self.region