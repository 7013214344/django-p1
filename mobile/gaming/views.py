from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def firing(request):
    return HttpResponse("we play here")