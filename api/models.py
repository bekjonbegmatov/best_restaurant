from django.db import models

# Create your models here.

class MenuModel(models.Model):
    img = models.ImageField(upload_to='menu/images')
    meal_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    pice = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.TimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Menu")
        verbose_name_plural = ("Menus")

    def __str__(self):
        return self.meal_name

