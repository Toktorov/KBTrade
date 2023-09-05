from django.shortcuts import render

from apps.settings.models import Setting, News

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    return render(request, 'about.html', locals())

def benefits(request):
    setting = Setting.objects.latest('id')
    return render(request, 'benefits.html', locals())

def stages(request):
    setting = Setting.objects.latest('id')
    return render(request, 'stages.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    return render(request, 'contact.html', locals())