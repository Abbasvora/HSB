from django.forms import ModelForm, fields
from .models import Temp_user

class Temp_userForm(ModelForm):
    class Meta:
        model = Temp_user
        fields = '__all__'
        labels = {
            'child_in_msb': 'Child studying in MSB',
            'year_of_passing': '10th Passing'
        }