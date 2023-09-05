from django.urls import path 

from apps.cars.views import car_detail


urlpatterns = [
    path('<int:id>/', car_detail, name='car_detail')
]