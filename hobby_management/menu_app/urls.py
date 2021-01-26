from django.urls import path
from .views import menu_main

urlpatterns = [
    path('', menu_main, name="menu"),
]