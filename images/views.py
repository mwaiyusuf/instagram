from django.shortcuts import render,redirect 
from django.http import HttpResponse,Http404,HttpResponseRedirect  
import datetime as dt 
# Create your views here.
def home(request):
  images = image.get_images()
  comments = Comment.get_comment()
  profile = profile.get_profile()


  current.user = request.user
  if request.method == 'POST':
    form = CommentForm(request.post)
    if form.is valid():
      comment = form.save(commit=False)
      comment.save()
    return redirect('home')

  else:
    form = CommetnForm()

  return render(request,"home.html",{"images":images,"comments":comments,"form":form,"profile":profile})
   
     