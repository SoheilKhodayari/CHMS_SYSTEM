__author__ = 'soheil'

from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^home/','Receptionist.views.home'),
)
