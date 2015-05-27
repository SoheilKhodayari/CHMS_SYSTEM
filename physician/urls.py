from django.conf.urls import patterns, url
from physician import views

urlpatterns = patterns('',

    url(r'^register$', views.register, name='doc_register'),
    url(r'^home$', views.home, name='doc_home'),

)
