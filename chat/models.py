from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000 ,default="")

class Message(models.Model):
    value = models.CharField(max_length=1000000, default="")
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000, default="")
    room = models.CharField(max_length=1000000, default="")


