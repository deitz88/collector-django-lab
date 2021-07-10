from django.forms import ModelForm
from .models import Mealtime

class MealtimeForm(ModelForm):
  class Meta:
    model = Mealtime
    fields = ['date', 'meal']