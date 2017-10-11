from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^([0-9]+)$', views.event_detail, name='event_detail'),
    url(r'^$', views.event_list, name='event_list'),
    url(r'^create$', views.create_event, name='create_event'),
    url(r'^do_create', views.do_create, name='do_create'),
]