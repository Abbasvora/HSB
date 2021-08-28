from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import User_accForm
from register.utils import is_admin
from register.models import User_acc
import xlwt
from django.http import HttpResponse
from register.decorators import admin_user
# Create your views here.

def login_page(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('hello')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            usr = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('hello')
            else:
                messages.error(request, "Username or Password is incorrect.")
        except:
            messages.error(request, "username doesnot exists.")
        
    context = {'page': page}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request, 'User was logged out')
    return redirect('hello')

def register_user(request):
    page = 'register'
    context = {'page': page}
    return render(request, 'users/login.html', context)

def hello(request):
    admin = is_admin(request=request)
    context = {"admin": admin}
    return render(request, 'users/hello.html', context)

def user_acc(request):
    update = True
    user = User.objects.get(username=request.user.username)
    acc = User_acc.objects.get(user=user)
    form = User_accForm(instance=acc)
    admin = is_admin(request=request)
    if request.method == "POST":
        form = User_accForm(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect("hello")
    
    context = {'form': form, "admin": admin, 'update':update}
    return render(request, "register/register_form.html", context)


@login_required(login_url='login')
@admin_user(allowed=['admin'])
def download(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	
    # headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = User_acc.objects.all() #dummy method to fetch data.
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.name, font_style)
		ws.write(row_num, 1, my_row.father_name, font_style)
		ws.write(row_num, 2, my_row.phone_number, font_style)
		ws.write(row_num, 3, my_row.profession, font_style)

	wb.save(response)
	return response
