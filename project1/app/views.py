from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def name(request):
    return HttpResponse('this is a test file')