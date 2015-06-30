import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from patient.models import Patient
from django.contrib.auth.models import User
from django.contrib import auth
from patient.models import *
from django.contrib.auth.decorators import login_required
from urllib import urlencode
from django.core.urlresolvers import reverse
from schedule.models import schedule

def register(request):
    try:
        if not (request.user.is_authenticated() and request.user.profile.user_type==0)  :
            return HttpResponse("server_message: Access Denied")
    except:
            return HttpResponse("server_message: Access Denied")
    c={}
    if request.method=="POST":
       try:
                birth=request.POST['birthday']
                fname=request.POST['first_name']
                lname=request.POST['last_name']
                user=User.objects.create_user(username=request.POST['username'] ,
                        password=request.POST['ssn'],
                        first_name=fname,
                        last_name=lname,
                        email=request.POST['email']
                        )
                user.save()

                patient=Patient(
                        user_type=2,
                        user=user,
                        firstname=fname,
                        lastname=lname,
                        Tel=request.POST['tel'],
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
                        postal_code=request.POST['postal_code']
                     )
                patient.save()
       except:
          try:
            if user: user.delete()
            if patient: patient.delete()
          except:
              pass
          return HttpResponse("An Error Has Occured During Registration, Since Required Fields Are Not  \
                              Entered Properly , Please Try Again" )


       c.update(csrf(request))
       return HttpResponseRedirect(reverse('rec_app:patients-list'))
    return render_to_response('patient/register.html',c,context_instance=RequestContext(request))


def home(request):
   try:
       if not (request.user.is_authenticated() and request.user.profile.user_type==2):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
   except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
   try:
       patient=Patient.objects.get(user=request.user)
   except:
       patient=None
   try:
       sch=schedule.objects.get(patient=patient)
   except:
       sch=None
   c={'patient':patient,'sch':sch}
   c.update(csrf(request))
   return render_to_response('patient/patient_home.html',c,context_instance=RequestContext(request))





