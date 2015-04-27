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

def register(request):
   c={}
   if request.method=="POST":
#     username=request.POST['username']
#     first_name=request.POST['first_name']
#     last_name=request.POST['last_name']
#     email=request.POST['email']
#     Tel=request.POST['tel']
#     ssn=request.POST['ssn']
      #b_day=request.POST.get('day','')
      #b_month=request.POST.get('month','')
     # b_year=request.POST.get('year','')
      #try:
     # birth=datetime.datetime(b_year,b_month,b_day)
      birth=request.POST['birthday']
      #except:
        # birth=None
#     age=request.POST['age']
#     marital_status=request.POST['marital_status']
#     marital_status_notes=request.POST['marital_status_notes']
#     occupation=request.POST['occupation']
#     occupation_notes=request.POST['occupation_notes']
#     country=request.POST['country']
#     city=request.POST['city']
#     district=request.POST['district']
#     street=request.POST['street']
#     alley=request.POST['alley']
#     building_no=request.POST['building_no']
#     postal_code=request.POST['postal_code']
      fname=request.POST['first_name']
      lname=request.POST['last_name']
      user=User.objects.create_user(username=request.POST['username'] ,
                password=request.POST['ssn'],
                first_name=fname,
                last_name=lname,
                email=request.POST['email']
                )
      user.save()


    
      patient=Patient(  #user_id=None,
                        user_type=2,
                        user=user,
                        firstname=fname,
                        lastname=lname,
                        Tel=request.POST['tel'],
                        ssn=request.POST['ssn'],
                        birthday=birth,
                        age=request.POST['age'],
                        marital_status=request.POST['marital_status'],
                        #marital_status_notes=request.POST['marital_status_notes'],
                        occupation=request.POST['occupation'],
                        #occupation_notes=request.POST['occupation_notes'],
                        country=request.POST['country'],
                        city=request.POST['city'],
                        district=request.POST['district'],
                        street=request.POST['street'],
                        alley=request.POST['alley'],
                        building_no=request.POST['building_no'],
                        postal_code=request.POST['postal_code']
                    )
      patient.save()
      c['birth']=birth
      c.update(csrf(request))
      return render_to_response('login_all.html',c,context_instance=RequestContext(request))
   return render_to_response('patient/register.html',c,context_instance=RequestContext(request))
    




def home(request):
    if not request.user.is_authenticated() or request.user.get_profile().user_type!=2:
        d = {'server_message':"Not Logged In."}
        query_str = urlencode(d)
        return HttpResponseRedirect('/login_all/?' +query_str)
    c={}
    c.update(csrf(request))
    return render_to_response('patient/patient_home.html',c,context_instance=RequestContext(request))





