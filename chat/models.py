from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# class User(AbstractUser):
#   username = models.CharField(max_length=100, blank=False, unique=True)
#   password = models.CharField(max_length=100, validators=[MinLengthValidator(10)], blank=False)

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True, blank=False)

class Room(models.Model):
  name = models.CharField(max_length=1000)

class Message(models.Model):
  value = models.CharField(max_length=1000000)
  date = models.DateTimeField(default=datetime.now, blank=True)
  user = models.CharField(max_length=1000000)
  room = models.CharField(max_length=1000000)