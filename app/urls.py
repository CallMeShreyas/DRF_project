from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('login', views.login),
    path('signup', views.signup),
    path('home', views.home),
    path('sent', views.sentmails),
    path('compose', views.compose),
    path('success', views.success)
]