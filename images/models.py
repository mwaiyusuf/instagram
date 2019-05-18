from django.db import models
from django.contrib.auth.models import user 
# Create your models here.
class Profile(models.Model):
  usesr = models.OneToOneField(User , on_delete=models.CASCADE,null=True)
  profile_photo=models.ImageField(upload_to='profiles/',null=True)
  bio=models,charField(max_length=240,null=True)


  def save_profile(self):
    self.save()


  @classmethod
  def get_profile(cls):
    profile = profile.objects.all()
    return profile 


  @classmethod
  def find_profile(cls,search_term):
    profile = profile.objects.filter(user__username__icontains=search_term)
    return profile 