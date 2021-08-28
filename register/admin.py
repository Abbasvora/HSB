from django.contrib import admin

# Register your models here.
from .models import Temp_user, User_acc

admin.site.register(Temp_user)
admin.site.register(User_acc)