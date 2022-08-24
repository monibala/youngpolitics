from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
     path('',views.index,name='index'),
     path('aboutus/',views.aboutus,name='aboutus'),
     path('blog/',views.blog,name='blog'),
     path('contact/',views.contact,name='contact'),
     path('message/',views.message,name='message'),
     path('our_team',views.ourteam,name='ourteam'),
     path('w_c_ec',views.wcec,name='wcec'),
     path('what_we_do',views.whatwedo,name='whatwedo'),
     
     path('enquiry', views.enquiry,name='enquiry'),
]