from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^(?P<username>[\w]+)/$', views.index, name='files'),
    # url(r'^show$',views.show,name='show_history')
    url(r'^(?P<username>[\w]+)/(?P<file_id>\d+)/$', views.medical_file, name='medical_file'),
    url(r'^(?P<username>[\w]+)/(?P<file_id>[\d]+)/medical_history$', views.medical_history, name='medical_history'),
    url(r'^(?P<username>[\w]+)/(?P<file_id>[\d]+)/progress_notes$', views.progress_notes, name='progress_notes'),
    url(r'^(?P<username>[\w]+)/(?P<file_id>[\d]+)/physician_orders$', views.physician_orders, name='phycisian_orders'),
    url(r'^(?P<username>[\w]+)/(?P<file_id>[\d]+)/unit_summary$', views.unit_summary, name='unit_summary'),
    url(r'^(?P<username>[\w]+)/create_file$', views.create_medical_file, name='create_medical_file'),
    url(r'^(?P<username>[\w]+)/create_file_index$', views.create_file, name='create_medical_file_index'),

)
