from django.shortcuts import render,redirect 
 from django.http import HttpResponse
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
# Create your views here.
 
   
     