def is_admin(request):
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
        print(request.user.groups.all()[0].name)
    if group == "admin":
            return True
    else:
        return False