from django.contrib import admin
from .models import City, Place, Flight
# Register your models here.
admin.site.register(City)
admin.site.register(Place)
admin.site.register(Flight)