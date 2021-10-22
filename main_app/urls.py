from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cities/', views.cities_index, name='cities'),
    
    path('cities/<int:city_id>', views.city_detail, name='detail'),

    path('cities/<int:city_id>/delete/', views.city_delete, name='delete'),
    path('cities/<int:city_id>/edit/', views.city_edit, name='edit'),
    path('cities/<int:city_id>/update', views.city_update, name='update'),
    path('cities/<int:city_id>/add_place', views.add_place, name='add_place'),
]