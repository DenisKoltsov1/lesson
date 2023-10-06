

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    email = models.EmailField(unique=False)
    viewsTime = models.IntegerField(default=0)