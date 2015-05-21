__author__ = 'soheil'
from django.conf.urls import patterns, url
from pharmacy.views import login

urlpatterns = patterns('',

    url(r'^login/$', login, name='login'),

)
