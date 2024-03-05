from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from .models import profiles

def home(request):
    return render(request,'social_media/home.html')

def profile(request):
    profiles_data = profiles.objects.all()  
    context = {'profiles': profiles_data} 
    return render(request, 'social_media/profile.html', context)
    
def create_post(request):
    return render(request,'social_media/create_post.html')

def about(request):
    return render(request,'social_media/about.html')

def contact(request):
    return render(request,'social_media/contact.html')

