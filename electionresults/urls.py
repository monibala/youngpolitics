from  django.urls import path

from .import views
urlpatterns=[
path('', views.general,name='general'),
path('melections/', views.melections, name='melections'),
path('upelections/', views.upelections, name='upelections'),
path('pollbooth/', views.pollbooth, name='pollbooth'),
path('election2022/', views.election2022, name='election2022'),
path('election2017/', views.election2017, name='election2017'),
path('election2012/', views.election2012, name='election2012'),
]