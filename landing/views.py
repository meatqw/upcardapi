from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.

def index(request):
    """Landos page"""
    context = {
        "page_info": ""
    }
    return render(request, 'landing/index.html', context)