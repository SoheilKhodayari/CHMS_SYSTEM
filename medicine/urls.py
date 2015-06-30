from django.conf.urls import patterns, url
from .views import medicine_list_view, MedicineDetailView, MedicineDeleteView
from .views import medicine_create_view, medicine_update_view,medicine_color_help


urlpatterns = patterns(
    '',
    url(r'^$', medicine_list_view, name='medicines-list'),
    url(r'colorHelp/$',medicine_color_help , name='color_help'),
    url(
        r'^create/$',
        medicine_create_view,
        name='medicines-create',
    ),
    url(
        r'^delete/(?P<code>[\w]+)/$',
        MedicineDeleteView.as_view(),
        name='medicines-delete',
    ),
    url(
        r'^update/(?P<code>[\w]+)/$',
        medicine_update_view,
        name='medicines-update',
    ),
    url(
        r'^(?P<code>[\w]+)/$',
        MedicineDetailView.as_view(),
        name='medicines-detail',
    ),
)
