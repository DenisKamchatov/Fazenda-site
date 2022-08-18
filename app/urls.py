from django.urls import path

from .views import *

urlpatterns = [
    path('', site, name="home"),
    path('gallery', photogallery, name="photogallery")
]
