from django.shortcuts import render,redirect 
from django.http import HttpResponse,Http404,HttpResponseRedirect  
import datetime as dt 
# Create your views here.
def welcome(request):
  return HttpResponse('welcome to the moringa tribune ')
 
   
     