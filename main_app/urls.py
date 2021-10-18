from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name='cities'),
    path('cities/<int:city_id>', views.city_detail, name='detail')
    
]