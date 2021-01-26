from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('login_app.urls')),
    path('menu/', include('menu_app.urls')),
    path('regist/', include('regist_app.urls')),
    path('admin/', admin.site.urls),
]

