
from django.contrib import admin
from django.urls import path, include   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecoapp/', include('ecoapp.urls')),  # Подключение маршрутов из вашего приложения "ecoapp"
]
