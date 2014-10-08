from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^verify', views.verify),
    url(r'^authenticate', views.authenticate),
)
