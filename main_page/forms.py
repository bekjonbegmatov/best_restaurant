from django.forms import ModelForm
from . import models
class Orderform(ModelForm):
    class Meta:
        model = models.BasketModel
        exclude = (
            'price' , 
            'meal_name' , 
            'quantity'
            )
        