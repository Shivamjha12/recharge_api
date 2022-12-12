from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
# ,LoginView
# Create your views here.
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from Accounts.forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from recharging_platform_project import settings
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import MaxValueValidator, MinValueValidator,FileExtensionValidator

# Create your views here.


class UserRegistration(CreateView):
    template_name ='registration/signup.html'
    form_class = CustomUserCreationForm
    success_url = 'login/'

def login(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request, username=username, password=password)
       if user is not None:
           auth_login(request, user)
           return redirect('/')
       if user is None:
           return redirect('/')
       else:
           messages.info(request, 'Username or password are not correct')
       

       if user is not None:
           auth_login(request, user)
           return redirect('/')
       else:

           messages.info(request, 'Username or password are not check username  correct')


    else:
        messages.info(request, 'Username or password are not correct')
        
    
    context = {}
    return render (request, 'registration/login.html', context)