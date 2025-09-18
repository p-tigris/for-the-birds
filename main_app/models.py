from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

RATINGS = (
    (1, '1 star'),
    (1.5, '1.5 stars'),
    (2, '2 stars'),
    (2.5, '2.5 stars'),
    (3, '3 stars'),
    (3.5, '3.5 stars'),
    (4, '4 stars'),
    (4.5, '4.5 stars'),
    (5, '5 stars')
)

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    description = models.TextField(max_length=800)
    birds = ArrayField(models.CharField(max_length=50), default=list, size=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


class Review(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(max_length=1, choices=RATINGS, default=RATINGS[0][0], null=True)
    date = models.DateField(null=True)
    text = models.TextField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    