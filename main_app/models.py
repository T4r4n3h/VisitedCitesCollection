from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

STYLE = (
    ('H', 'Historical'),
    ('S', 'Scientific'),
    ('V', 'View'),
    ('I', 'Interesting')
)
class Flight(models.Model):
    airline = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    def __str__(self):
        return self.airline

    def get_absolute_url(self):
        return reverse('flights_detail',kwargs={'pk':self.id})    

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField()
    rank = models.IntegerField()
    flights = models.ManyToManyField(Flight)
    user = models.ForeignKey(User, on_delete =models.CASCADE)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    description = models.TextField(max_length=150)
    style = models.CharField(
        max_length=1,
        choices=STYLE,
        #I want the default value of the style to be "I" as Interesting
        default= STYLE[3][0]       
    )
    city = models.ForeignKey(City, on_delete=models.CASCADE)