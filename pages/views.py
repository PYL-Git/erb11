from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
#as templates directory is set in settings.py, no need to add here
def about(request):
    return render(request,'pages/about.html')