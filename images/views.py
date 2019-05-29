from django.conf import settings
import datetime as dt
from django.shortcuts import render,redirect 
from django.http import HttpResponse,Http404
from django.conf.urls import url,include
from django.contrib.auth import authenticate, login, logout
from .forms import PostForm
from .models import Profile, Image
from django.contrib.auth.models import User
from . import models
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    all_images = Image.objects.all()
    next = request.GET.get('next')
    if next: return redirect(next)
    return render(request, 'display/home.html',  {"all_images":all_images})

@login_required(login_url='/accounts/login/')
def explore(request):
    return render(request, 'display/all.html')

@login_required(login_url='/accounts/login/')
def notification(request):
    return render(request, 'display/notification.html') 
     
@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'display/user.html')
    
# @login_required(login_url='/accounts/login/')
# def login(request):
#     return render(request, 'registration/login.html')

# def logout(request):
#     return render(request, 'registration/logout.html')



@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    p = Profile.objects.filter(id=current_user.id).first()
    imageuploader_profile = Image.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form_post = PostForm(request.POST,request.FILES)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.imageuploader_profile
            # deleted = d
            post.save()
            return redirect('upload')
    else:
        form_post =PostForm
    return render(request,'upload.html', {"form_post": form_post})
# deleted display/
# deleted request

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form_post = PostForm(request.POST,request.FILES)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post_user=current_user
            form_post.save()
            return redirect('new_post')
    else:
        form_post =PostForm(instance=request.user)
    return render(request, 'display/new_post.html')