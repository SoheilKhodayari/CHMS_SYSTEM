from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='system_home'),
    url(r'^show$',views.show,name='show_history')

)
