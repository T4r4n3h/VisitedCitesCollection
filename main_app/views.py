from django.shortcuts import render

# Create your views here.
from .models import City

#Define the home views 
# def home(request):
#     return HttpResponse('<h1> Hello to Cities Ive been to</h1>')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    
def cities_index(request):
    cities = City.objects.all()
    print('this is the list of cities:', cities)
    return render(request, 'cities/index.html',{
        'cities': cities,
    })

def city_detail(request, city_id):
    city = City.objects.get(id=city_id)
    print('this is the city: ', city)
    return render(request, 'cities/detail.html',{
        'city': city,
    })

