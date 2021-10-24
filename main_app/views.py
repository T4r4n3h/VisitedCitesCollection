from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
# from django.shortcuts import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .models import City, Place, Flight
from .forms import PlaceForm

#Define the home views 
# def home(request):
#     return HttpResponse('<h1> Hello to Cities Ive been to</h1>')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




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
    lst_of_places = city.place_set.all()
    print('this is the list of places:', lst_of_places)
    print('this is the city: ', city)

    place_form = PlaceForm()

    return render(request, 'cities/detail.html',{
        'city': city,
        'place_form': place_form
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

def add_place(request, city_id):
    Place.objects.create(
      name=request.POST['name'],
      description=request.POST['description']  
    )
    return redirect(f'/cities/{city_id}')


class FlightList(ListView):
    models = Flight
    def get_queryset(self):
        return Flight.objects.all()

class FlightDetail(DetailView):
    model = Flight

class FlightCreate(CreateView):
    model = Flight
    fields = '__all__'

class FlightUpdate(UpdateView):
    model = Flight
    fields = ['airline', 'origin']

class FlightDelete(DeleteView):
    model = Flight
    success_url = '/flights/'