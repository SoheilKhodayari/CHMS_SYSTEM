__author__ = 'soheil'

from django.conf.urls import patterns, url
from .views import patient_list_view , delete_guardian, set_schedule_view,update_schedule_view,delete_schedule
from .views import patient_create_view, patient_update_view,detail,delete,allocate_ward_view,update_ward_view



urlpatterns = patterns('',
    url(r'^search/','Receptionist.views.search_rec',name='rec_search'),

    url(r'^$', patient_list_view, name='patients-list'),
    url(
        r'^create/$',
        patient_create_view,
        name='patients-create',
    ),
    # url(
    #     r'^delete/(?P<pk>[\w]+)/$',
    #     PatientDeleteView.as_view(),
    #     name='patients-delete',
    # ),
    # url(
    #     r'^update/(?P<pk>[\w]+)/$',
    #     patient_update_view,
    #     name='patients-update',
    # ),
    # url(
    #     r'^(?P<username>[\w]+)/$',
    #     PatientDetailView.as_view(),
    #     name='patients-detail',
    # ),
    url(
        r'^delete/(?P<username>[\w]+)/$',
        delete,
        name='patients-delete',
    ),
    url(
        r'^update/(?P<username>[\w]+)/$',
        patient_update_view,
        name='patients-update',
    ),
    url(
        r'^(?P<username>[\w]+)/$',
        detail,
        name='patients-detail',
    ),
        url(
        r'^allocate_ward/(?P<username>[\w]+)/$',
        allocate_ward_view,
        name='allocate-ward',
    ),
         url(
        r'^update_ward/(?P<username>[\w]+)/$',
        update_ward_view,
        name='update-ward',
    ),
        url(
        r'^delete_ward/(?P<username>[\w]+)/$',
        delete_guardian,
        name='delete-ward',
    ),

        url(
        r'^set_schedule/(?P<username>[\w]+)/$',
        set_schedule_view,
        name='set-schedule',
    ),
        url(
        r'^update_schedule/(?P<username>[\w]+)/$',
        update_schedule_view,
        name='update-schedule',
    ),
        url(
        r'^delete_schedule/(?P<username>[\w]+)/$',
        delete_schedule,
        name='delete-schedule',
    ),
)