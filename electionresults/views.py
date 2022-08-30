from django.shortcuts import render

from dashboard.models import elec_res

# Create your views here.
def general(request):
    data = elec_res.objects.order_by('year')
    return render(request,'general.html',{'data':data})

def melections(request):
    return render(request, 'melections.html')
def upelections(request):
    return render(request, 'upelections.html')
def pollbooth(request):
    return render(request, 'pollbooth.html')