from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp\index.html",  # Relative path from the 'templates' folder to the template file
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )