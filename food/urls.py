from django.urls import path
from food.views import *
app_name='foodie'
urlpatterns=[
 path('biriyani/',biriyani,name='biriyani')   
]