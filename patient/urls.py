from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='patient_index'),
    url(r'^register$', views.register, name='patirnt_register'),
    
)
