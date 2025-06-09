from django.shortcuts import render

def home(request):
    return render(request, 'homepage/home.html')

def endpoints(request):
    return render(request, 'homepage/endpoints.html')
