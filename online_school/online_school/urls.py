from django.contrib import admin
from django.urls import path
from API.api import app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', app.urls)
]
