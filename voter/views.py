from django.shortcuts import render

from dashboard.models import voterlist

# Create your views here.
def print(request):
    obj = voterlist.objects.all()
    return render(request,'print.html',{'obj':obj})