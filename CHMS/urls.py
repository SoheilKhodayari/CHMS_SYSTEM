from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from CHMS import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CHMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'hospital/$', include('hospital.urls')),
    url(r'pharmacy/', include('pharmacy.urls')),
    url(r'history/', include('history_records.urls',namespace='history_records')),
    url(r'app/', include('androidApp.urls',namespace='android_app')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient/',include('patient.urls',namespace='patient_app')),
    url(r'^$', views.firstpage , name = 'firstpage'),
    url(r'^SystemHomePage/',views.SystemHomePage,name='SystemHomePage'),
    url(r'^PatientSearch/',views.PatientSearch,name='PatientSearch'),
    url(r'^rec/',include('Receptionist.urls', namespace='rec_app')),
    url(r'^login_all/',views.login,name='login_all'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^medicine/', include('medicine.urls',namespace='medicine_app')), # pharmacy

    url(r'^reports/',views.get_reports,name='reports'),

    
)
