from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',

    url(r'^login$', views.login, name='system_home'),
    url(r'^show$',views.get_diagnose_file,name='get_diagnose_file'),
    url(r'^get_list$',views.get_patient_list,name='get_patient_list'),
    url(r'^get_patient_details',views.get_patient_details,name='get_patient_detail'),
    url(r'^get_unit_summary$',views.get_unit_summary,name='get_unit_summary'),
    url(r'^get_physician_orders$',views.get_physician_order,name='get_physician_orders'),
    url(r'^set_physician_order$',views.set_physician_order,name='set_physician_order'),
    url(r'^get_progress_notes$',views.get_progress_note,name='get_progress_notes'),
    url(r'^set_progress_note$',views.set_progress_note,name='set_progress_note'),
    url(r'^get_medical_history$',views.get_medical_history,name='get_medicla_history'),
    url(r'^get_doctor_details$',views.get_physician_details,name='get_physician_details'),

)



