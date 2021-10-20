from django.shortcuts import redirect, render

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

def city_delete(request, city_id):
    print( 'we wanna delete!')
    del_city = City.objects.get(id = city_id)
    print(f'this is the city we are gonna delete, {del_city}')
    del_city.delete()
    return redirect('/cities')

def city_edit(request, city_id):
    print( 'we wanna edit')
    ed_city = City.objects.get(id=city_id)
    print( f'this is the city we are gonna edit, {ed_city}')
    return render(request, 'cities/edit.html',{
        'city': ed_city
    })
def city_update(request, city_id):
    print( 'we wanna update')
    up_city = City.objects.get(id=city_id) 
    print( f'this is the city we are gonna update, {up_city}')
    print ( f'this is the req.post,{request.POST}')
    up_city.name = request.POST['name']
    up_city.country = request.POST['country']
    up_city.img = request.POST['img']
    up_city.description = request.POST['description']
   
    up_city.save()
    return redirect('/cities/')