from django.urls import path
from .views import *

urlpatterns = [
    path("", gpt, name="gpt")
]