from django.shortcuts import render, redirect
from .forms import Temp_userForm
from .models import Temp_user, User_acc
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import time
from django.core.mail import message, send_mail
from django.conf import settings
from .decorators import admin_user
from .utils import is_admin
# Create your views here.

def register_user(request):
    form = Temp_userForm()
    admin = is_admin(request=request)
    if request.method == "POST":
        form = Temp_userForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("hello")
    
    context = {'form': form, "admin": admin}
    return render(request, "register/register_form.html", context)


@login_required(login_url='login')
@admin_user(allowed=['admin'])
def list_user(request):
    admin = is_admin(request=request)
    users = Temp_user.objects.all()
    page = "register"
    context = {'users': users, 'page': page, "admin": admin}
    return render(request, "register/list_user.html", context)

@login_required(login_url='login')
@admin_user(allowed=['admin'])
def add_user(request, pk):
    user = Temp_user.objects.get(id=pk)
    usr = User_acc()
    usr.name = user.name
    usr.phone_number = user.phone_number
    usr.whatsapp_number = user.whatsapp_number
    usr.profession = user.profession
    usr.email = user.email
    usr.qualification = user.qualification
    usr.its_id = user.its_id
    usr.blood_group = user.blood_group
    usr.maritial_status = user.maritial_status
    usr.child_in_msb = user.child_in_msb
    usr.year_of_passing = user.year_of_passing
    ts = str(time.time()).split('.')[0][-5:]
    password = user.email.split('@')[0] + ts
    add = User.objects.create_user(username=user.its_id,
                                 email=user.email,
                                 password=password)

    usr.user = add
    usr.save()
    message = f' Use the given user id and password to login to your account\n Username: {user.its_id}\n Password: {password}'
    send_mail(
        'Welcome To HSB Godhra',
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False
    )
    user.delete()
    
    return redirect("list-user")

@login_required(login_url='login')
@admin_user(allowed=['admin'])
def delete_user(request, pk):
    
    user = Temp_user.objects.get(id=pk)
    user.delete()
    
    return redirect("list-user")


@login_required(login_url='login')
@admin_user(allowed=['admin'])
def view_member(request):
    admin = is_admin(request=request)
    users = User_acc.objects.all()
    page = "view"
    print(users)
    context = {'users': users, 'page': page, "admin": admin}
    return render(request, "register/list_user.html", context)