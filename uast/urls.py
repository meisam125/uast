
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', include('login.urls')),
    path('louast/', include('louast.urls')),
    path('befor90/', include('befor90.urls')),
    path('admin/', admin.site.urls),
]
