from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import MyUser
from django.contrib.auth.views import LoginView as LoginViewContrib , LogoutView as LogoutViewContrib
from .forms import RegisterForm


class RegisterView(CreateView):
    model = MyUser
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = '/login/'


class LoginView(LoginViewContrib):
    template_name = 'user/login.html'

    # self.request.user


class LogoutView(LogoutViewContrib):
    pass