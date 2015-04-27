from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from patient.models import Patient
from django.http import HttpResponse
from Receptionist.views import *
from django.views.decorators.csrf import csrf_exempt


def firstpage(request):
    c={}
    c.update(csrf(request))
    return render_to_response('firstpage.html',c,context_instance=RequestContext(request))

# @csrf_exempt
# def login(request):
#     c={'error':'','user':''}
#     if request.method == "POST":
#         username = request.POST.get('username', '') #retunr '' if no username
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request,user)
#             #return HttpResponseRedirect('/rec/home')
#             c['user']=user
#             if user.username[0]=='p' :
#                 return render_to_response('patient/patient_home.html',c,context_instance=RequestContext(request))
#             elif user.username[0]=='r'  :
#                 return render_to_response('Receptionist/Receptionist_home.html',c,context_instance=RequestContext(request))
#             else:
#
#                 c['error'] = 'No Part'
#                 return render_to_response('login_all.html',c,context_instance=RequestContext(request))
#         else:
# 			c['error'] = 'wrong credentials try again'
# 			return render_to_response('login_all.html',c,context_instance=RequestContext(request))
#
#     c.update(csrf(request))
#     return render_to_response('login_all.html',c,context_instance=RequestContext(request))

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponse('Successfully Logged Out')


@csrf_exempt
def login(request):
    c={'error':'','user':''}
    if request.method == "POST":
        username = request.POST.get('username', '') #retunr '' if no username
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            #return HttpResponseRedirect('/rec/home')
            c['user']=user
            if user.get_profile().user_type==2 :
                return render_to_response('patient/patient_home.html',c,context_instance=RequestContext(request))
            elif user.get_profile().user_type==0  :
                return render_to_response('Receptionist/Receptionist_home.html',c,context_instance=RequestContext(request))
            else:

                c['error'] = 'No Part'
                return render_to_response('login_all.html',c,context_instance=RequestContext(request))
        else:
			c['error'] = 'wrong credentials try again'
			return render_to_response('login_all.html',c,context_instance=RequestContext(request))

    c.update(csrf(request))
    return render_to_response('login_all.html',c,context_instance=RequestContext(request))


