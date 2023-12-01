from django.shortcuts import render

# Create your views here.

def myhub(request):
    return render(request, 'myhub/dashboard.html')