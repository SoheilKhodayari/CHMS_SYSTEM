from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from patient.models import Patient
from django.http import HttpResponse
from Receptionist.views import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from Receptionist.search import *

def firstpage(request):
    if request.method=='POST':
        if request.method.POST.get('home'):
            return HttpResponseRedirect('SystemHomePage')
        if request.method.POST.get('search'):
            return HttpResponseRedirect('PatientSearchPage')
    c={}
    c.update(csrf(request))
    return render_to_response('firstpage.html',c,context_instance=RequestContext(request))

def SystemHomePage(request):
    c={}
    c.update(csrf(request))
    return render_to_response('SystemHomePage.html',c,context_instance=RequestContext(request))

def PatientSearch(request):
    if request.method == 'GET':
        if request.GET.get("submit_search_btn"): 
            query_string = ''
            found_entries = None
            if ('q' in request.GET) and request.GET['q'].strip():
                query_string = request.GET['q']

                entry_query = get_query(query_string, ['firstname', 'lastname','ssn','user__username','parent_hospital__Hospital_Name'])

                found_entries = Patient.objects.filter(entry_query)


            return render_to_response('PatientSearch.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))


    return render_to_response('PatientSearch.html',{},context_instance=RequestContext(request))


@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@csrf_exempt
def login(request):
    c={'error':'','user':''}
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            c['user']=user
            try:
                if user.profile.user_type==2 :
                    return HttpResponseRedirect(reverse("patient_app:patient_home"))
                elif user.profile.user_type==0  :
                    return HttpResponseRedirect(reverse("rec_app:rec_search"))
                elif user.profile.user_type==6 :
                    return HttpResponseRedirect(reverse("doc_app:doc_home"))
                else:

                    c['error'] = 'No Part'
                    return render_to_response('login_all.html',c,context_instance=RequestContext(request))
            except:
                    c['error'] = 'wrong credentials try again'
		    return render_to_response('login_all.html',c,context_instance=RequestContext(request))
                
        else:
			c['error'] = 'wrong credentials try again'
			return render_to_response('login_all.html',c,context_instance=RequestContext(request))

    c.update(csrf(request))
    return render_to_response('login_all.html',c,context_instance=RequestContext(request))


def get_reports(request):
    hospitals=request.POST.getlist('hospitals')
    return render(request,'CHMS/reports.html')
