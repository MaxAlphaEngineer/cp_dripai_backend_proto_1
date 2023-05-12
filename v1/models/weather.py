from django.db import models

from v1.models import User



class Weather(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.JSONField(default={})
    current = models.JSONField(default={})
    forecast = models.JSONField(default={})

    def response(self):
        return {
            "id": self.id,
            "location": self.location,
            "current": self.current,
            "forecast": self.forecast,
        }




