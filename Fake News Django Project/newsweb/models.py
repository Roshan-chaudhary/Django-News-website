
from django.db import models

# Create your models here.
class Contact(models.Model):
 name=models.CharField(max_length=100)
 email=models.EmailField(max_length=100)
 phone=models.CharField(max_length=100)
 concern=models.TextField(max_length=100)
 
 
 
class Image(models.Model):
 photo = models.ImageField(upload_to="myimage")
 title=models.CharField(max_length=100)
 des=models.CharField( max_length=150)
 date = models.DateTimeField(auto_now_add=True)
 
 
 
 
 
 