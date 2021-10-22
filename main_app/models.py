from django.db import models

# Create your models here.

STYLE = (
    ('H', 'Historical'),
    ('S', 'Scientific'),
    ('V', 'View'),
    ('I', 'Interesting')
)


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    description = models.TextField()
    rank = models.IntegerField()
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