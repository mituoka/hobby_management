from django.contrib import admin
from django.urls import path, include

print(1)
urlpatterns = [
    path('', include('login_app.urls')),
    path('admin/', admin.site.urls),
]

