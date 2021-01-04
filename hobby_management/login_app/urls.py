from django.urls import path
from .views import login

urlpatterns = [
    path('', login.main_login, name='test'),
    path('login/', login.main_login, name="test"),
]