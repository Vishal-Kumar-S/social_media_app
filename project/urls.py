
from django.contrib import admin
from django.urls import path,include
from App1 import views

urlpatterns = [
    path('e_commerce/',include('e_commerce.urls')),
    path('social_media/',include('social_media.urls')),
    path('admin/', admin.site.urls)

]
