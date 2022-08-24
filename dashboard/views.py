from email.policy import default
from http.client import HTTPResponse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as dj_login, logout
from dashboard.forms import NewUserForm
from django.contrib import messages
from django.contrib import messages as sms

from dashboard.models import elec_res, my_team, voterlist
from home.models import blog_detail
# Create your views here.
def administrator(request):
    return render(request,'login.html')
def login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # dj_login(request, user)
            return render(request, 'dashboardindex.html')

        else:
            messages.success(request, 'Username or Password is incorrect!')
        
    template = 'login.html'
    context = {}
    return render(request, template, context)

    # if request.user.is_authenticated and request.user.is_superuser:
    #     return redirect('dashboardindex')
    # if request.method=="POST":
    #     print(request.POST,"this is working")
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     USER = authenticate(request,username=username, password=password)
    #     if USER is not None:
    #         # login(request, USER)
    #         if request.user.is_superuser:
    #             return JsonResponse({'status':'ok','msg':'Login Success','next':request.GET.get('next'),'type':'success'})
    #         return JsonResponse({"status":'invaliduser','msg':'invalid user','type':'danger'})
    #     return JsonResponse({"status":'invaliduser','msg':'Invalid Credentials','type':'danger'})
    # return render(request,'login.html')
def logout(request):
    # if request.method == 'POST':
    #     logout(request)
    # return redirect('login')
    if request.user.is_authenticated and request.user.is_superuser:
   
        try:
            logout(request)
            sms.success(request,'Logout Successfully.')
            return redirect('login')
        except Exception as e:
            sms.warning(request,'something went wrong !')
            return redirect('login')
    else:
        return redirect('login')

def register(request):
    form = NewUserForm()
    if request.method == 'POST':

        form = NewUserForm(request.POST)
        if form.is_valid():

            form.save()
            
            
            return redirect('login')

    else:
        form = NewUserForm()

    return render(request, 'register.html', {'form': form })

def dashboard(request):
    return render(request,'dashboardindex.html')


def news(request):
    return render(request,'news.html')


def results(request):
    return render(request,'results.html')
def elections(request):
    return render(request,'elections.html')
def survey(request):
    return render(request,'survey.html')
def blogs(request):
    return render(request, 'blogs.html')
def add_voter(request):
    if request.user. is_authenticated and request.user.is_superuser:
        obj = voterlist.objects.all()
        dl = request.POST.get('delete')
        print(dl)
        edit = request.POST.get('edit')
        print(edit)
    if request.method=="POST":
        if dl!=None:    
            ob = voterlist.objects.filter(id=dl)
            ob.delete()
        elif edit!=None:
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            dob = request.POST.get('dob')
            address = request.POST.get('address')
            images = request.FILES.get('images')
            voter = voterlist.objects.filter(id=edit)
            if len(voter)>0:
                obj = voter[0]
                if(len(name))>0:
                    obj.name=name
                if len(age)>0:
                    obj.age=age
                if len(gender)>0:
                    obj.gender=gender
                if images:
                    obj.images=images
                obj.save()
            sms.success(request,'Updated.')
            return redirect('add_voter')    
        else:
            if request.method=="POST":
            # name = request.POST.get('name',"default value")
            # gender = request.POST.get('gender',"default value")
                name = request.POST['name']
                images = request.FILES.get('images')
                gender = request.POST['gender']
                age = request.POST['age']
                dob = request.POST['dob']
                address = request.POST['address']
                voter = voterlist(name=name,age=age,gender=gender,dob=dob,address=address,images=images)
                voter.save()
    
    return render(request, 'add_voter.html', {'obj':obj})
    # return render(request,'add_voter.html')

def ad_blog(request):
    # if request.user.is_authenticated and request.user.is_superuser:
        blgdata = blog_detail.objects.all()
        team_data = my_team.objects.all()
        dl = request.POST.get('delete')
        edit = request.POST.get('bedit')
        print(edit)
        if request.method=="POST":
            if dl!=None:
                del_obj = blog_detail.objects.filter(id=dl)
                # print(del_obj)
                del_obj.delete()
            elif edit!=None:
                bname = request.POST.get('bname')
                description = request.POST.get('description')
                images = request.FILES.get('images')
                blog_data = blog_detail.objects.get(id=edit)
                print(blog_data)
                if len(blog_data)>0:
                    obj = blog_data[0]
                    if(len(bname))>0:
                        obj.bname=bname
                    if(len(description))>0:
                        obj.description = description
                    if images:
                        obj.bimage=images
                    obj.save()
                # sms.success(request,'Updated.')
                # return redirect('ad_blog')   
            # else:
                    
            #   return redirect('ad_blog')  

        return render(request, 'blogs.html',{'blgdata':blgdata})
def add_blog(request):
    if request.method=='POST':
        bname = request.POST['bname']
        description = request.POST['description']
        bimage = request.FILES['bimage']
        data = blog_detail(bname=bname,description=description,bimage=bimage)
        data.save()
        return redirect('ad_blog')
    else:
        
        return render(request,'add_blog.html')
def ad_general(request):
    # if request.user. is_authenticated and request.user.is_superuser:
        elecdata = elec_res.objects.all()
        dl = request.POST.get('delete')
        edit = request.POST.get('edit')
        print(edit)
        if request.method=='POST':
            if dl!=None:
                obj = elec_res.objects.filter(id=dl)
                obj.delete()
            elif edit!=None:
                print(edit)
                party = request.POST.get('party')
                seats = request.POST.get('seats')
                vote = request.POST.get('vote')
                elec_data = elec_res.objects.filter(id=edit)
                print(elec_data)
                if len(elec_data)>0:
                    ob = elec_data[0]
                    if len(party)>0:
                        ob.party=party
                        print(ob.party)
                    if len(seats)>0:
                        ob.seats=seats
                    if len(vote)>0:
                        ob.vote=vote
                    ob.save()
        return render(request,'ad_general.html',{'elecdata':elecdata})
    
               

def ad_team(request):
    # if request.user.is_authenticated and request.user.is_superuser:
        team_data = my_team.objects.all()
        dl=request.POST.get('delete')
        edit = request.POST.get('edit')
        if request.method=='POST':
            if dl!=None:

                obj = my_team.objects.filter(id=dl)
                obj.delete()
            elif edit!=None:
                name = request.POST.get('name')
                designation = request.POST.get('designation')
                images = request.FILES.get('images')
                data = my_team.objects.filter(id=edit)
                
                if len(data)>0:
                    ob = data[0]
                    if len(name)>0:
                        ob.name=name
                        print(ob.name)
                    if len(designation)>0:
                        ob.designation=designation
                    if images:
                        ob.images=images
                    ob.save()
                return redirect('ad_team')
        return render(request, 'ad_team.html',{'team_data':team_data})
  
        
        
               
   
def add_team(request):
    if request.method=='POST':
        name = request.POST['name']
        designation = request.POST['designation']
        images = request.FILES.get('images')
        add_data = my_team(name=name,designation=designation,images=images)
        add_data.save()
        return redirect('ad_team')
    else:
        return render(request,'add_team.html')
def add_genresults(request):
    if request.method=='POST':
        year=request.POST['year']
        party=request.POST['party']
        seats=request.POST['seats']
        vote=request.POST['vote']
        data = elec_res(year=year,party=party,seats=seats,vote=vote)
        data.save()
        return redirect('ad_general')
    else:
        # return redirect('add_genresults') 
        return render(request,'add_genresults.html')