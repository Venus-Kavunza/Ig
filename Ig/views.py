from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http.response import Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from .forms import *
from django.contrib import messages
from .models import Image, Comments, Profile, Follow
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views import generic 
from cloudinary.forms import cl_init_js_callbacks
from django.views.decorators.csrf import csrf_exempt
from .email import send_welcome_email
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            name=form.cleaned_data['fullname']
            email=form.cleaned_data['email']
           
            send_welcome_email(name,email)

            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('instagram:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='/accounts/login/')
def home_page(request):
    current_user = request.user
    posts = Image.objects.all()
   
    user = User.objects.get(username=current_user.username)
    users = User.objects.exclude(username=current_user.username).exclude(is_superuser=True)
  
    ctx = {
        'posts':posts,
        'user':user,
        'users':users,     
        }

    return render(request,'instagram/home.html',ctx)

