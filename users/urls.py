from django.urls import path
from django.urls.resolvers import URLPattern 
from . import views


urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('account/', views.user_acc, name='account'),
    path('download/', views.download, name='download'),
    path('', views.hello, name="hello"),
]

