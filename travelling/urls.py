from django.urls import path
from travelling.views import *
app_name='ootyhills'
urlpatterns=[
 path('ooty/',ooty,name='ooty')   
]