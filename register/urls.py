from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.register_user, name="register_user"),
    path('list_user/', views.list_user, name="list-user"),
    path('view_member/', views.view_member, name="view-member"),
    path('add_user/<str:pk>', views.add_user, name="add-user"),
    path('delete_user/<str:pk>', views.delete_user, name="delete-user"),
]
