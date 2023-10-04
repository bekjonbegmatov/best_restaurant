from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='main'),
    path('rules' , views.rules , name='rules'),
    path('backet' , views.backet , name='basket'),
    path('create' , views.create_order , name='create_order'),
    path('delete/<int:order_id>' , views.delete_order , name='delete_order'),
]