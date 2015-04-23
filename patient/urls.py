from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^login$', views.p_login, name='patient_login'),
    url(r'^register$', views.register, name='patirnt_register'),
    
)
