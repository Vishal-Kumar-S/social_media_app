
from django.contrib import admin
from django.urls import path,include
from App1 import views

urlpatterns = [
    path('',include('App1.urls')),
    path('admin/', admin.site.urls)
]
