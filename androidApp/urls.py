from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^login$', views.login, name='system_home'),
    url(r'^show$',views.get_diagnose_file,name='get_diagnose_file'),

)



