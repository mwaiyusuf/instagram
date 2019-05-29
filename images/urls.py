from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render, redirect
# from . import views 

 
urlpatterns=[
  url(r'^$',views.index, name='index'),
  url(r'^all/$',views.explore,name ='explore'),
  url(r'^notification',views.notification,name ='notification'),
  url(r'^profile',views.profile,name ='profile'),
  # url(r'^logout',views.index,{'next_page': 'accounts:login'}, name='logout'),
  url(r'^logout',views.profile,name='profile'),
  # url('^login',views.login,name='login'),
  # url('^upload/$',views.upload,name ='upload'),
    url(r'^new_post/$',views.new_post,name ='new_post'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)