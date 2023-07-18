from django.shortcuts import render

def index(request):
    """Landos page"""
    context = {
        "page_info": ""
    }
    return render(request, 'landing/index.html', context)