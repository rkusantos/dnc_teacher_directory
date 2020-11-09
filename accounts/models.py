from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.conf import settings

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return f"{self.username}"


class UserImage(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return f"{self.username}"