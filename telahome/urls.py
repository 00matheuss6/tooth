
from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.view_home, name='home')
    
]

