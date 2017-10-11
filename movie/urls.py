from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.movie_list, name='movie_list'),
    url(r'^([0-9]+)/$', views.movie_detail, name='movie_detail'),
]