from . import views
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from .views import *
urlpatterns = [
    path('', RegisterView.as_view(), name='registration'),
    path('', LoginView.as_view(), name='login'),
    path('', LogoutView.as_view(), name='logout'),
]