from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
# from . import views 

 
urlpatterns=[
  url('^$',views.index, name='index'),
  url('^explore',views.explore,name ='explore'),
  url('^notification',views.notification,name ='notification'),
  url('^profile',views.profile,name ='profile'),
  url('^login',views.login,name ='login'),
  url('^logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
  url('^upload',views.upload,name ='upload'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)