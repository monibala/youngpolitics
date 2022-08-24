from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from dashboard.models import my_team

# Create your views here.
def aboutus(request):
    return render(request, 'aboutus.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    # print("request")
    if request.method=='POST':
        print("Welnk nd")
       
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        service = request.POST['service']
        comment = request.POST['comment']
        # con = contact(name=name,email=email,number=number,service=service,comment=comment)
        # con.save()
        msg = (f'name:{name}\n email:{email}\n service:{service}\n message:{comment}')
        # print("workinh")
        send_mail(name,msg,email,[settings.EMAIL_HOST_USER],fail_silently=False)
        messages.success(request,'Your Message Send Successfully.')
        # print(send_mail)
    return render(request, 'contact.html')
def index(request):
    if request.method=='POST':
        print("Welnk nd")
       
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        service = request.POST['service']
        comment = request.POST['comment']
        # con = contact(name=name,email=email,number=number,service=service,comment=comment)
        # con.save()
        msg = (f'name:{name}\n email:{email}\n service:{service}\n message:{comment}')
        # print("workinh")
        send_mail(name,msg,email,[settings.EMAIL_HOST_USER],fail_silently=False)
        messages.success(request,'Your Message Send Successfully.')
    return render(request, 'index.html')
def message(request):
    return render(request, 'message.html')
def ourteam(request):
    team_data = my_team.objects.all()
    return render(request, 'our_team.html',{'team_data':team_data})
def wcec(request):
    return render(request, 'w_c_ec.html')
def whatwedo(request):
    return render(request, 'what_we_do.html')
def enquiry(request):
    return render(request,'enquiry.html')