from django.shortcuts import render

# Create your views here.
def all_index(request):
    return render(request, 'newapp/all_index.html')



