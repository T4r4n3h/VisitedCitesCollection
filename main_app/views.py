from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#Define the home views 
# def home(request):
#     return HttpResponse('<h1> Hello to Cities Ive been to</h1>')

def home(request):
    return render(request, 'about.html')

class City:
    def __init__(self, name, country, rank):
        self.name = name
        self.country = country
        self.rank = rank
        


cities = [
    City('Paris', 'France', 4),
    City('Valencia', 'Spain', 5),
    City('New York', 'United States', 4)

]






def cities_index(request):
    return render(request, 'cities/index.html', {'cities':cities})
