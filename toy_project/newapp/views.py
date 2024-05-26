from django.shortcuts import render
from .models import NewVariety

# Create your views here.
def all_index(request):
    return render(request, 'newapp/all_index.html')


def all_category(request):
    variety = NewVariety.objects.all()
    return render(request, 'newapp/all_index.html', {'veriety': 'veriety'})
