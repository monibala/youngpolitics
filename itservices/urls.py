from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
    path('', views.fbpromotion, name='fbpromotion'),
    path('twitter/', views.twitter, name='twitter'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('youtube/', views.youtube, name='youtube'),
    path('promotional/', views.promotional, name='promotional'),
    path('transitional/', views.transitional, name='transitional'),
    path('esms/', views.esms, name='esms'),
    path('otp/', views.otp, name='otp'),
    path('broadcast/', views.broadcast, name='broadcast'),
    path('dtmf/', views.dtmf, name='dtmf'),
    path('texttovoice/', views.texttovoice, name='texttovoice'),
    path('ivr/', views.ivr, name='ivr'),
    path('tollfree/', views.tollfree, name='tollfree'),
    path('callalert/', views.callalert, name='callalert'),
    path('virtual/', views.virtual, name='virtual'),
]
