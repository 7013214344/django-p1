from audio.views import *
from django.urls import path

urlpatterns = [
    path("spotify/",spotify,name='spotify'),
]