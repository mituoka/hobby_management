from django.urls import path
from .views import login,logout,menu,regist

urlpatterns = [
    path('login/', login.main_login, name="login"),
    path('menu/', menu.menu_main, name="menu"),
    path('regist/', regist.regist_main, name="regist"),
    path('logout/', logout.logoutfunc, name="logout"),
    path('menu/test_ajax_app', menu.test_ajax_app, name='test_ajax_app'),
]