from django.db import models
from django.contrib.auth.models import user 
# Create your models here.
class Profile(models.Model):
  usesr = models.OneToOneField(User , on_delete=models.CASCADE,null=True)
  profile_photo=models.ImageField(upload_to='profiles/',null=True)
  bio=models,charField(max_length=240,null=True)