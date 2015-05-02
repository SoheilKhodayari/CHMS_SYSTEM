from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^(?P<patient_id>[0-9]+)$', views.index, name='system_home'),
    # url(r'^show$',views.show,name='show_history')
    url(r'^(?P<patient_id>[0-9]+)/medical_history$', views.medical_history, name='medical_history'),
    url(r'^(?P<patient_id>[0-9]+)/progress_notes$', views.progress_notes, name='progress_notes'),
    url(r'^(?P<patient_id>[0-9]+)/physician_orders$', views.physician_orders, name='phycisian_orders'),
    url(r'^(?P<patient_id>[0-9]+)/unit_summary$', views.unit_summary, name='unit_summary'),

)
