from django.urls import path
from .views import login,logout,menu,regist,app_detail

urlpatterns = [
    path('login/', login.main_login, name="login"),
    path('menu/', menu.menu_main, name="menu"),
    path('regist/', regist.regist_main, name="regist"),
    path('logout/', logout.logoutfunc, name="logout"),
    path('menu/search_category', menu.search_category, name='search_category'),
    path('menu/delete_image', menu.delete_image, name='delete_image'),
    path('app_detail/', app_detail.app_detail_main, name="app_detail"),
]