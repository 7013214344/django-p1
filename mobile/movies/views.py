from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def watch(request):
    return HttpResponse("we watch movies here")