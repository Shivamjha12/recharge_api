from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import CustomUserManager
# Create your models here.
class CustomUser(AbstractBaseUser,PermissionsMixin):
    USERNAME_FIELD     = 'email'
    Name               = models.CharField(max_length=100,blank = True, null=True)
    phone_no           = models.CharField(max_length=10, blank = True, null=True,unique=True)
    email              = models.EmailField(('email adress'),unique=True)
    is_staff           = models.BooleanField(default=False)
    is_active          = models.BooleanField(default=True)
    date_joined        = models.DateField(default=timezone.now)
    fields=[email]
    EMAIL_FIELD        = 'email'
    REQUIRED_FIELDS=[]
    objects = CustomUserManager()

        
