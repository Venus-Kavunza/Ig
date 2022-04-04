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
#from .email import send_welcome_email
# Create your views here.


