from django.shortcuts import render

# Create your views here.
def gpt(req):
    return render(req, "gpt.html")