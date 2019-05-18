from django.shortcuts import render,redirect 
from django.http import HttpResponse,Http404,HttpResponseRedirect  
import datetime as dt 
# Create your views here.
def home(request):
  images = image.get_images()
  comments = comment.get_comment()
  profile = profile.get_profile()

  
   
     