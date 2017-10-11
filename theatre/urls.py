from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.theatre_list, name='theatre_list'),
    url(r'^([0-9]+)$', views.theatre_detail, name='theatre_detail'),
]
