from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! You are at Neural-Navigator")


def about(request):
    return HttpResponse("Hello, world! You are at Neural-Navigator About section")


def contact(request):
    return HttpResponse("Hello, world! You are at Neural-Navigator Contact section ")

