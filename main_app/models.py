from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    pass

class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)