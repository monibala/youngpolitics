from django.shortcuts import render

# Create your views here.
def website(request):
    return render(request, 'website.html')
def jantadarbar(request):
    return render(request, 'jantadarbar.html')
def ems(request):
    return render(request, 'ems.html')