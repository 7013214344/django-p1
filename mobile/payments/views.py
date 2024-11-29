from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def pay(request):
    return HttpResponse("we do payments here")