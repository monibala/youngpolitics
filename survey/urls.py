from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
    path('poll/', views.poll, name='poll'),
    path('surveyresearch/', views.surveyresearch, name='surveyresearch'),
    path('dtdsurvey/', views.dtdsurvey, name='dtdsurvey'),
    path('boothlsbel/', views.boothlabel, name='boothlabel'),
    path('wrcc/', views.wrcc, name='wrcc'),
    path('voteappeal/', views.voteappeal,name='voteappeal'),
    path('campaign/', views.campaign,name='campaign'),
    path('campaignmanage/', views.campaignmanage,name='campaignmanage'),
    path('docfilm/', views.docfilm,name='docfilm'),
]