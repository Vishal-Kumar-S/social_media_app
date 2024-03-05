from django.urls import path,include
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('create_post/', views.create_post, name='create_post'),
    path('About/', views.about, name='about'),
    path('Contact/', views.contact, name='contact')
]