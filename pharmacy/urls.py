__author__ = 'soheil'
from django.conf.urls import patterns, url
from pharmacy import views

urlpatterns = patterns('',

    url(r'^login/$', views.login, name='login'),

)
