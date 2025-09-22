from django.db import models
from django.urls import reverse
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

TAGS = (
    ('City Park', 'City Park'),
    ('State Park', 'State Park'),
    ('National Park', 'National Park'),
    ('Wildlife Refuge', 'Wildlife Refuge'),
    ('Zoo', 'Zoo'),
    ('Aviary', 'Aviary'),
    ('Other', 'Other')
)

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    tag = models.CharField(max_length=50, choices=TAGS, default=TAGS[0][0])
    image = models.URLField(max_length=200, blank=True, null=True, help_text="(Please insert image URL of location)")
    description = models.TextField(max_length=800)
    birds = ArrayField(models.CharField(max_length=50), default=list, size=None, help_text="(Include relevant bird species; separate them by comma)")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"location_id": self.id})
    
    


class Review(models.Model):
    title = models.CharField(max_length=50)
    rating = models.FloatField(max_length=1, choices=RATINGS, default=RATINGS[0][0], blank=True, null=True)
    date = models.DateField('Date Visited', blank=True, null=True)
    text = models.TextField(max_length=800)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
    
    def get_absolute_url(self):
        return reverse("location-detail", kwargs={"location_id": self.location.id})