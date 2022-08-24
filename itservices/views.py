from django.shortcuts import render

# Create your views here.
def fbpromotion(request):
    return render(request,'fbpromotion.html')

def twitter(request):
    return render(request,'twitter.html')

def whatsapp(request):
    return render(request,'whatsapp.html')

def youtube(request):
    return render(request,'youtube.html')