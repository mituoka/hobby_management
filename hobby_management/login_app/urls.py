from django.urls import path
from .views import login

urlpatterns = [
    path('login/', login.main_login, name="login"),
    # path('singup/', login.singup, name="singup"),
]