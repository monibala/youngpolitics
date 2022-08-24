from django.conf import settings
from  django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.conf.urls import static
urlpatterns=[
     path('', views.administrator,name='login'),
     path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),
     path('register/', views.register, name='register'),
     # path('recover-password/', views.recoverpassword, name='recover-password'),
     path('blogs/', views.blogs, name='blogs'),
     path('dashboardindex/',views.dashboard,name='dashboardindex'),
     path('survey/',views.survey,name='survey'),
     path('results/',views.results,name='results'),
     path('elections/', views.elections, name='elections'),
     path('news', views.news, name='news'),
     path('add_voter', views.add_voter, name='add_voter'),
     path('ad_blog', views.ad_blog, name='ad_blog'),
     path('ad_general',views.ad_general, name='ad_general'),
     path('ad_team', views.ad_team, name='ad_team'),
     path('add_genresults/',views.add_genresults, name='add_genresults'),
     path('add_team', views.add_team, name='add_team'),
     path('add_blog', views.add_blog, name='add_blog'),
]
# if settings.DEBUG:
#     urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
