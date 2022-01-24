from django.db import models
from .forms import NameForm


# Create your models here.

class register(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
