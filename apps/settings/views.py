from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html', locals())

def benefits(request):
    return render(request, 'benefits.html', locals())

def stages(request):
    return render(request, 'stages.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())