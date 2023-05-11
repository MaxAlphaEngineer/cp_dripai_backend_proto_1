from django.db import models


class Region(models.Model):
    region = models.CharField(max_length=50, choices=[
        ("Andijan","Andijan"),
        ("Bukhara","Bukhara"),
        ("Ferghana","Ferghana"),
        ("Jizzakh","Jizzakh"),
        ("Namangan","Namangan"),
        ("Navoiy","Navoiy"),
        ("Kashkadarya","Kashkadarya"),
        ("Samarkand","Samarkand"),
        ("Sirdarya","Sirdarya"),
        ("Surkhandarya","Surkhandarya"),
        ("Tashkent region","Tashkent region"),
        ("Tashkent","Tashkent"),
        ("Khorezm","Khorezm"),
        ("Karakalpakstan Republic","Karakalpakstan Republic"),
    ])

    def __str__(self):
        return self.region


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.CharField(max_length=128)

    def __str__(self):
        return self.region
