from django.urls import path
from .views import regist_main

urlpatterns = [
    path('', regist_main, name="regist"),
]