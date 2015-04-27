from django.conf.urls import patterns, url
from patient import views

urlpatterns = patterns('',

    url(r'^register$', views.register, name='patirnt_register'),
    url(r'^home$', views.home, name='patient_home'),
    
)
