__author__ = 'soheil'

from django.conf.urls import patterns, url



urlpatterns = patterns('',
    url(r'^login/$','Receptionist.views.rec_login'),
    url(r'^logout/$','Receptionist.views.rec_logout'),
    url(r'^home/','Receptionist.views.home'),
)
