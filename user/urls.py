from django.urls import path
from . import views
urlpatterns = [
    path('' , views.signup , name='user'),
    # logoutuser
    path('logout' , views.logoutuser , name='logoutuser'),
    path('login' , views.loginuser , name='login'),
]