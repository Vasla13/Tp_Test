from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100, verbose_name="Marque")
    purchase_date = models.DateField(verbose_name="Date d'achat")
    number_of_seats = models.IntegerField(verbose_name="Nombre de places")
    description = models.TextField(verbose_name="Description")
    length = models.FloatField(verbose_name="Longueur du véhicule")
    has_air_conditioning = models.BooleanField(default=False, verbose_name="Climatisation")

    def __str__(self):
        return f"{self.brand} ({self.purchase_date})"
