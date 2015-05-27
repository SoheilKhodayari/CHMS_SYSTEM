from models import *
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.core.context_processors import csrf
from urllib import urlencode
from patient.models import *
from django.core.urlresolvers import reverse


def register(request):
   c={}
   if request.method=="POST":
       #try:
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

            physician=Physician(
                        user_type=6,
                        user=user,
                        Tel=request.POST['tel'],
                        ssn=request.POST['ssn'],
                        birthday=birth,
                        age=request.POST['age'],
                        marital_status=request.POST['marital_status'],
                        is_staff_head=request.POST['is_staff_head'],
                        country=request.POST['country'],
                        city=request.POST['city'],
                        district=request.POST['district'],
                        street=request.POST['street'],
                        alley=request.POST['alley'],
                        building_no=request.POST['building_no'],
                        postal_code=request.POST['postal_code'],
                        specialty=request.POST.get('speciality','ent'),
                        graduation_university_name=request.POST['graduation_university_name'],
                        graduation_university_country=request.POST['graduation_university_country'],
                        graduation_university_city=request.POST['graduation_university_city'],
                        degree=request.POST['degree'])
            physician.save()
       #except:
            #try:
                #if user:
                #    user.delete()
               # if physician:
                #    physician.delete()
            #except:
            #    pass
            #return HttpResponse("An Error Has Occured During Registration, Since Required Fields Are Not    \
                            #    Entered Properly , Please Try Again" )


            c.update(csrf(request))
            return HttpResponseRedirect(reverse('rec_app:rec_search'))
   return render_to_response('physician/register.html',c,context_instance=RequestContext(request))



def home(request):
   try:
       if not (request.user.is_authenticated() and request.user.profile.user_type==6):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
   except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
   try:
       doc=Physician.objects.get(user=request.user)
   except:
       doc=None

   c={'doc':doc}
   c.update(csrf(request))
   return render_to_response('physician/physician_home.html',c,context_instance=RequestContext(request))











