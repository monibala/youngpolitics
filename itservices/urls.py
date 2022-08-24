from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
urlpatterns=[
    path('', views.fbpromotion, name='fbpromotion'),
    path('twitter/', views.twitter, name='twitter'),
    path('whatsapp/', views.whatsapp, name='whatsapp'),
    path('youtube/', views.youtube, name='youtube'),
]
