from django.contrib import admin
from django.urls import path
from . import views 

app_name = "blog"

urlpatterns = [
    
    path('', views.index_view, name="index_view"),
    path('login', views.login_view, name="login_view"),
    path('registration', views.registration_view, name="registration_view"),
    path('homepage/<username>', views.homepage_view, name="homepage_view"),
    path('logout', views.logout_view, name="logout_view"),
    
]



