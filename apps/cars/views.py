from django.shortcuts import render

from apps.settings.models import Setting
from apps.cars.models import Car, CarImage

# Create your views here.
def car_detail(request, id):
    setting = Setting.objects.latest('id')
    car = Car.objects.get(id = id)
    images = CarImage.objects.filter(car = id)
    return render(request, 'car_detail.html', locals())