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

def promotional(request):
    return render(request,'promotional.html')
def transitional(request):
    return render(request,'transitional.html')
def esms(request):
    return render(request,'esms.html')
def otp(request):
    return render(request,'otp.html')
def broadcast(request):
    return render(request,'broadcast.html')

def dtmf(request):
    return render(request,'dtmf.html')
def texttovoice(request):
    return render(request,'texttovoice.html')
def ivr(request):
    return render(request,'ivr.html')
def tollfree(request):
    return render(request,'tollfree.html')
def callalert(request):
    return render(request,'callalert.html')
def virtual(request):
    return render(request,'virtual.html')