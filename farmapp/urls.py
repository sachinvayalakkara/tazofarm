from django.urls import path
from . import views
urlpatterns = [
    path('home',views.fn_home),
    path('login',views.fn_login),
    path('register',views.fn_register),
    path('menu',views.fn_menu),
    path('tower',views.fn_showtower),
    path('addtower',views.fn_addtower),
    path('viewtower',views.fn_viewtower)
]