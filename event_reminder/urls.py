from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reminder.urls')),  # Uygulamanın API URL’lerini dahil ediyoruz
]