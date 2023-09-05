from django.urls import path 

from apps.settings.views import index, about, benefits, stages, contact


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('benefits/', benefits, name='benefits'),
    path('stages/', stages, name='stages'),
    path('contact/', contact, name='contact'),
]