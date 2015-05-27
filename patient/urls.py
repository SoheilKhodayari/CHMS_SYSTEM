from django.conf.urls import patterns, url
from patient import views

urlpatterns = patterns('',

    url(r'^register$', views.register, name='patient_register'),
    url(r'^home$', views.home, name='patient_home'),
    
)
