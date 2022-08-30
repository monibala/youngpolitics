from django.shortcuts import render

from dashboard.models import voterlist

# Create your views here.
def print(request):
   
    return render(request,'print.html')