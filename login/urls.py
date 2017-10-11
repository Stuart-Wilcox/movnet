from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login_form, name='login'),
    url(r'^dologin$', views.login_user, name='dologin'),
    url(r'^dologout$', views.logout_user, name='dologout'),
]
