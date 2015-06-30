from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from Receptionist.search import *
from patient.models import Patient
from django.contrib.auth.models import User
from urllib import urlencode
from patient.models import Guardian
from models import Receptionist



def search_rec(request):
    try:
        if not (request.user.is_authenticated() and request.user.profile.user_type==0)  :
            d = {'server_message':"Not Logged In."}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' +query_str)
    except:
            d = {'server_message':"not logged in"}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' +query_str)
    if request.method == 'GET':
        rec=Receptionist.objects.get(user=request.user)
        if request.GET.get("submit_search_button"): # if search submit button clicked
            query_string = ''
            found_entries = None
            if ('q' in request.GET) and request.GET['q'].strip():
                query_string = request.GET['q']

                entry_query = get_query(query_string, ['firstname', 'lastname','patient_section','patient_room','user__username'])

                found_entries = Patient.objects.filter(entry_query)
                found_entries=found_entries.filter(parent_hospital= rec.hospital)

            return render_to_response('Receptionist/rec_search.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))

    #To Do: Handle Other parts of Receptionsit Here

    return render_to_response('Receptionist/rec_search.html',{},context_instance=RequestContext(request))

###########################################################################################################

from django.shortcuts import render_to_response
from rest_framework import viewsets


from patient.models import Patient
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    filter_fields = (
        'user'
        'username',
        'firstname',
        'lastname',
        'gender',
        'patient_section',
        'patient_room',
        'gender',
    )

    def pre_save(self, obj):
        user = self.request.user
        obj.superuser = user
        super(PatientViewSet, self).pre_save(obj)


def patient_list_view(request):
    try:
        if not (request.user.is_authenticated() and request.user.profile.user_type==0)  :
            d = {'server_message':"Not Logged In."}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' +query_str)
    except:
            d = {'server_message':"not logged in"}
            query_str = urlencode(d)
            return HttpResponseRedirect('/login_all/?' +query_str)

    patients = None
    search = request.GET.get("search", False)
    rec=Receptionist.objects.get(user=request.user)
    if search:
        try:
            patients = Patient.objects.filter(username__icontains=search) | \
                Patient.objects.filter(firstname__icontains=search) | \
                Patient.objects.filter(lastname__icontains=search)
        except Exception, e:
            patients = None
    else:
        patients = Patient.objects.all()
        patients=patients.filter( parent_hospital= rec.hospital)
    ctx = {'patients': patients}

    return render_to_response(
        'Receptionist/list.html',
        ctx,
        context_instance=RequestContext(request),
    )


# class PatientDetailView( DetailView):
#     model = Patient
#     pk_url_kwarg = 'username'
#     template_name = 'Receptionist/detail.html'
def detail(request,username):
    patient=Patient.objects.get(username=username)
    try:
        ward=Guardian.objects.get(patient_detail=patient)
    except:
        ward=None
    try:
        sch=schedule.objects.get(patient=patient)
    except:
            sch=None
    ctx = {'patient': patient,'ward':ward,'sch':sch}


    return render_to_response(
        'Receptionist/detail.html',
        ctx,
        context_instance=RequestContext(request),
    )


# solo como superuser
# class PatientDeleteView( DeleteView):
#     model = Patient
#     success_url = reverse_lazy('rec_app:patients-list')
#     #pk_url_kwarg = 'username'
#     template_name = 'Receptionist/delete.html'

def delete(request,username):
    patient=Patient.objects.get(username=username)
    ctx = {'patient': patient}
    if request.method=="POST":
        patient.delete()
        return HttpResponseRedirect(reverse('rec_app:patients-list'))
    return render_to_response(
        'Receptionist/delete.html',
        ctx,
        context_instance=RequestContext(request),
    )

def record_patient(request):
      birth=request.POST['birthday']
      fname=request.POST['first_name']
      lname=request.POST['last_name']
      usrname=request.POST['username']
      user=User.objects.create_user(username=usrname ,
                password=request.POST['ssn'],
                first_name=fname,
                last_name=lname,
                email=request.POST['email']
                )
      user.save()

      section=request.POST['section']
      room=request.POST['room']
      patient=Patient(  username=usrname,
                        user_type=2,
                        user=user,
                        firstname=fname,
                        lastname=lname,
                        Tel=request.POST['Tel'],
                        ssn=request.POST['ssn'],
                        birthday=birth,
                        age=request.POST['age'],
                        marital_status=request.POST['marital_status'],
                        occupation=request.POST['occupation'],
                        country=request.POST['country'],
                        city=request.POST['city'],
                        district=request.POST['district'],
                        street=request.POST['street'],
                        alley=request.POST['alley'],
                        building_no=request.POST['building_no'],
                        postal_code=request.POST['postal_code'],
                        gender=request.POST['gender'],
                        patient_room=room,
                        patient_section=section
                    )
      patient.save()

      return patient


def patient_create_view(request):
    #if request.user.is_authenticated() and request.user.is_superuser:
        if request.method == "POST":
            patient = record_patient(request)
            if patient:
                return HttpResponseRedirect(
                    reverse('rec_app:patients-list')
                )

        return render_to_response(
            'Receptionist/create.html',
            context_instance=RequestContext(request),
        )




def update_patient(request, username):

      section=request.POST['section']
      room=request.POST['room']
      birth=request.POST['birthday']
      fname=request.POST['first_name']
      lname=request.POST['last_name']
      email=request.POST['email']
      Tel=request.POST['Tel']
      ssn=request.POST['ssn']
      age=request.POST['age']
      marital_status=request.POST['marital_status']
      occupation=request.POST['occupation']
      country=request.POST['country']
      city=request.POST['city']
      district=request.POST['district']
      street=request.POST['street']
      alley=request.POST['alley']
      building_no=request.POST['building_no']
      postal_code=request.POST['postal_code']
      gender=request.POST['gender']

      #patient = get_object_or_404(Patient, pk=username)
      try:
            patient=Patient.objects.get(username=username)
      except:
            patient=None

      patient.user.first_name=fname
      patient.user.last_name=lname
      patient.user.email=email


      patient.Tel=Tel
      patient.ssn=ssn
      patient.age=age
      patient.marital_status=marital_status
      patient.occupation=occupation
      patient.country=country
      patient.city=city
      patient.district=district
      patient.street=street
      patient.alley=alley
      patient.building_no=building_no
      patient.postal_code=postal_code
      patient.gender=gender
      patient.birthday=birth
      patient.patient_room=room
      patient.patient_section=section
      patient.save()
      return patient


def patient_update_view(request, username):

        if request.method == "POST":
            patient = update_patient(request,username)
            if patient:
                return HttpResponseRedirect(
                    reverse('rec_app:patients-list')
                )

        #patient = get_object_or_404(Patient, pk=username)
        try:
            patient=Patient.objects.get(username=username)
        except:
            patient=None

        ctx = {'patient': patient}

        return render_to_response(
            'Receptionist/update.html',
            ctx,
            context_instance=RequestContext(request),
        )

################################################################## Guardian Allocation

def allocate_ward(request,username):

    name=request.POST['name']
    relation=request.POST['relation']
    phone=request.POST['phone']
    patient=Patient.objects.get(username=username)
    gr=Guardian(guardian_name=name , relation_to_guardian=relation, guardian_phone=phone ,patient_detail=patient)
    gr.save()
    return gr

def allocate_ward_view(request, username):

        if request.method == "POST":
            ward = allocate_ward(request,username)
            if ward:
                return HttpResponseRedirect(
                    "/rec/"+username
                )

        #patient = get_object_or_404(Patient, pk=username)
        # try:
        #     patient=Patient.objects.get(username=username)
        #     ward=Guardian.objects.get(patient_detail=patient)
        # except:
        #     ward=None
        #
        # ctx = {'ward': ward}
        ctx={}
        return render_to_response(
            'Receptionist/allocate_ward.html',
            ctx,
            context_instance=RequestContext(request),
        )
def update_ward(request,username):
    name=request.POST['name']
    relation=request.POST['relation']
    phone=request.POST['phone']
    patient=Patient.objects.get(username=username)
    gr=Guardian.objects.get(patient_detail=patient)
    gr.guardian_name=name
    gr.relation_to_guardian=relation
    gr.guardian_phone=phone
    gr.save()
    return gr
def update_ward_view(request,username):
        if request.method == "POST":
            ward = update_ward(request,username)
            if ward:
                return HttpResponseRedirect(
                    "/rec/"+username
                )

        try:
            patient=Patient.objects.get(username=username)
            ward=Guardian.objects.get(patient_detail=patient)
        except:
            ward=None

        ctx = {'patient':patient,'ward': ward,'username':username}

        return render_to_response(
            'Receptionist/ward_allocation_update.html',
            ctx,
            context_instance=RequestContext(request),
        )

def delete_guardian(request,username):
    patient=Patient.objects.get(username=username)
    gr=Guardian.objects.get(patient_detail=patient)
    ctx = {'patient': patient,'ward':gr}
    if request.method=="POST":
        gr.delete()
        return HttpResponseRedirect("/rec/"+username)
    return render_to_response(
        'Receptionist/delete_ward.html',
        ctx,
        context_instance=RequestContext(request),
    )

##################################################################  Schedule
from schedule.models import schedule

def set_schedule(request,username):
    patient=Patient.objects.get(username=username)

    event=request.POST['event']
    event_date=request.POST['event_date']
    event_time=request.POST['event_time']
    related_division=request.POST['related_division']
    description=request.POST['description']

    sch=schedule(patient=patient,event=event,event_date=event_date,event_time=event_time,related_division=related_division,description=description)
    sch.save()
    return sch
def set_schedule_view(request,username):
        if request.method == "POST":
            sch = set_schedule(request,username)
            if sch:
                return HttpResponseRedirect(
                    "/rec/"+username
                )
        ctx={}
        # try:
        #     patient=Patient.objects.get(username=username)
        #     sch=schedule.objects.get(patient=patient)
        # except:
        #     sch=None
        #
        # ctx = {'patient':patient,'sch': sch,'username':username}

        return render_to_response(
            'Receptionist/set_schedule.html',
            ctx,
            context_instance=RequestContext(request),
        )
def update_schedule(request,username):
    patient=Patient.objects.get(username=username)

    event=request.POST['event']
    event_date=request.POST['event_date']
    event_time=request.POST['event_time']
    related_division=request.POST['related_division']
    description=request.POST['description']
    sch=schedule.objects.get(patient=patient)
    sch.event=event
    sch.event_date=event_date
    sch.event_time=event_time
    sch.related_division=related_division
    sch.description=description
    sch.save()
    return sch
def update_schedule_view(request,username):
        if request.method == "POST":
            sch = update_schedule(request,username)
            if sch:
                return HttpResponseRedirect(
                    "/rec/"+username
                )

        try:
            patient=Patient.objects.get(username=username)
            sch=schedule.objects.get(patient=patient)
        except:
            sch=None

        ctx = {'patient':patient,'sch': sch,'username':username}

        return render_to_response(
            'Receptionist/update_schedule.html',
            ctx,
            context_instance=RequestContext(request),
        )

def delete_schedule(request,username):
    patient=Patient.objects.get(username=username)
    sch=schedule.objects.get(patient=patient)
    ctx = {'patient': patient,'sch':sch}
    if request.method=="POST":
        sch.delete()
        return HttpResponseRedirect("/rec/"+username)
    return render_to_response(
        'Receptionist/delete_schedule.html',
        ctx,
        context_instance=RequestContext(request),
    )
