from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BasketModel(models.Model):
    user = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)    
    meal_name = models.CharField(max_length=50)
    quantity = models.FloatField()

    class Meta:
        verbose_name = ("Basket")
        verbose_name_plural = ("Baskets")

    def __str__(self):
        return self.meal_name
