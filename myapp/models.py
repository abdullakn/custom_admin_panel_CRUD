
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.





class MyUserData(AbstractUser):
    phone=PhoneNumberField()
    place=models.CharField(max_length=50)

