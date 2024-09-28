from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):

    username= None
    email = models.EmailField(max_length=255, unique=True)
    phone_number= models.CharField(max_length=100, unique=True)
    user_Bio= models.CharField(max_length=50)
    user_profile_img= models.ImageField(upload_to='profile')

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects= UserManager()

    def __str__(self):
        return self.email