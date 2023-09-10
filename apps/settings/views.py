from django.shortcuts import render, redirect

from apps.settings.models import Setting, News, Benefit, Review, Contact, Team
from apps.cars.models import Car, CarImage

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    random_cars = Car.objects.all().order_by('?')[:3]
    cars = Car.objects.all()
    benefits = Benefit.objects.all().order_by('?')
    reviews = Review.objects.all().order_by('?')
    return render(request, 'index.html', locals())

def about(request):
    setting = Setting.objects.latest('id')
    benefits = Benefit.objects.all().order_by('?')
    reviews = Review.objects.all().order_by('?')
    teams = Team.objects.all()
    return render(request, 'about.html', locals())

def benefits(request):
    setting = Setting.objects.latest('id')
    benefits = Benefit.objects.all().order_by('?')
    cars = Car.objects.all()
    return render(request, 'benefits.html', locals())

def stages(request):
    setting = Setting.objects.latest('id')
    return render(request, 'stages.html', locals())

def contact(request):
    setting = Setting.objects.latest('id')
    return render(request, 'contact.html', locals())

def send_contact(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    user_contact = Contact.objects.create(name=name, phone=phone)
    return redirect('index')

def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news = News.objects.get(id = id)
    return render(request, 'news_detail.html', locals())