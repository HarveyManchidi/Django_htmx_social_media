from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
#class User(models.Model):
#   name = models.Charfield()


class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(max_length=400,blank=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    photo = models.ImageField(upload_to='profile_picture')
    followers = models.ManyToManyField(User, blank=True,related_name='followers')
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile',args=[self.pk])