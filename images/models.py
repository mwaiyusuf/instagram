from django.db import models
 
# Create your models here.
class Categories(models.Model):
   name=models.CharField(max_length=30)
#returning a unicode of any object 
#object to string 
   def __str__(self):
     return self.name 

class Location(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
      return self.name 

class Image(models.Model):
  name=models.CharField(max_length=50)
  description=models.TextField()
  instagram_image=models.ImageField(upload_to='base-images/',blank=True)
  categories=models.ManyToManyField(categories)
  location=models.ForeignKey(location)

  @classmethod
  def all_images(self):
    return Image.objects.all()
    

