from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("Hello, world! You are at Neural-Navigator")


def about(request):
    return HttpResponse("Hello, world! You are at Neural-Navigator About section")


def contact(request):
    return HttpResponse("Hello, world! You are at Neural-Navigator Contact section ")

