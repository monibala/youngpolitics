from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
    path('', views.website, name='website'),
    path('jantadarbar/', views.jantadarbar, name='jantadarbar'),
    path('ems/', views.ems, name='ems'),
]