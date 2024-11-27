from django.urls import path
from gaming.views import *
urlpatterns = [
    path('firing/',firing,name='firing'),
]