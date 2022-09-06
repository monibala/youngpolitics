from django.shortcuts import render

# Create your views here.
def poll(request):
    return render(request,'poll.html')

def surveyresearch(request):
    return render(request, 'survey and research.html')

def dtdsurvey(request):
    return render(request, 'dtdsurvey.html')

def boothlabel(request):
    return render(request, 'boothlabel.html')

def wrcc(request):
    return render(request, 'wrcc.html')

def voteappeal(request):
    return render(request, 'voteappeal.html')

def campaign(request):
    return render(request, 'campaign.html')

def docfilm(request):
    return render(request, 'docfilm.html')

def campaignmanage(request):
    return render(request, 'campaignmanage.html')
