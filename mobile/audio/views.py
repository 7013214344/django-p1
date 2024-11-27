from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def spotify(request):
    return HttpResponse("we listen songs here")