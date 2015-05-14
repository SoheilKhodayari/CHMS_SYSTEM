from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^(?P<username>[\w]+)$', views.index, name='system_home'),
    # url(r'^show$',views.show,name='show_history')
    url(r'^(?P<username>[\w]+)/medical_history$', views.medical_history, name='medical_history'),
    url(r'^(?P<username>[\w]+)/progress_notes$', views.progress_notes, name='progress_notes'),
    url(r'^(?P<username>[\w]+)/physician_orders$', views.physician_orders, name='phycisian_orders'),
    url(r'^(?P<username>[\w]+)/unit_summary$', views.unit_summary, name='unit_summary'),

)
