from django.forms import ModelForm, fields
from register.models import User_acc

class User_accForm(ModelForm):
    class Meta:
        model = User_acc
        exclude = ['user']