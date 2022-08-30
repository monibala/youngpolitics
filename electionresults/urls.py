from  django.urls import path

from .import views
urlpatterns=[
path('', views.general,name='general'),
path('melections/', views.melections, name='melections'),
path('upelections/', views.upelections, name='upelections'),
path('pollbooth/', views.pollbooth, name='pollbooth'),
]