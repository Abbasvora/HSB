from django.shortcuts import render
from django.http import HttpResponse, request

def admin_user(allowed=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed:
                 return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page")
        return wrapper_func
    return decorator











































































