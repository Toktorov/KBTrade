from django.urls import path 

from apps.settings.views import index, about, benefits, stages, contact, send_contact, news_detail


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('benefits/', benefits, name='benefits'),
    path('stages/', stages, name='stages'),
    path('contact/', contact, name='contact'),
    path('send_contact/', send_contact, name='send_contact'),
    path('news/<int:id>/', news_detail, name='news_detail'),
]