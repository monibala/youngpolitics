from django.shortcuts import render

from dashboard.models import elec_res

# Create your views here.
def general(request):
    data = elec_res.objects.order_by('year')
    return render(request,'general.html',{'data':data})