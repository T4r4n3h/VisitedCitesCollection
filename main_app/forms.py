from django.forms import ModelForm
from .models import Place

class PlaceForm(ModelForm):
  class Meta:
    model = Place# <-- the model we're using
    fields = ['name', 'description']