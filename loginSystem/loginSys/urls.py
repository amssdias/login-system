from django.urls import path
from . import views

urlpatterns = [
    path('login/', views._login, name="login"),
    path('logout/', views._logout, name="logout"),
    path('register/', views.register, name="register"),
    path('main/', views.main, name="main"),
]