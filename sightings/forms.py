from django.forms import ModelForm
from .models import Squirrel

class SquirrelForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age']

class SquirrelForm_(ModelForm):
    class Meta:
        model = Squirrel
        fields = '__all__'
