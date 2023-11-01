from django.shortcuts import render
from .models import *

# Create your views here.
contacts = Contacts.objects.all()

def index(req):
    context = {"contacts": contacts}
    return render(req, "index.html", context=context)

def items(req):
    objects = Objacts.objects.all()
    context = {
        "objacts": objects,
        "contacts": contacts
        }
    return render(req, "items-menu.html", context=context)

def ssl(req):
    return render(req, "UBl4DVG7D02YX77B37ePMVeiHZ6UqseI2C_O33Up4mc")