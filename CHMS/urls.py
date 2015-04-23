from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CHMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('hospital.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient/',include('patient.urls')),
    url(r'^$', views.firstpage , name = 'firstpage'),
    url(r'^rec/',include('Receptionist.urls')),
    
)
