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
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient/',include('patient.urls')),
    url(r'^$', views.firstpage , name = 'firstpage'),
    url(r'^rec/',include('Receptionist.urls')),
    url(r'^login_all/',views.login,name='login_all'),
    url(r'^logout/',views.logout,name='logout'),
    url(r'^medicine/', include('medicine.urls',namespace='medicine_app')), # pharmacy

    
)
