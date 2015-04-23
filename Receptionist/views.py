from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import auth
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from search import *
from patient.models import Patient
from django.contrib.auth.models import User


def rec_login(request):
    context = {'error':''}
    if request.method == 'POST':
        username = request.POST.get('username', '') #retunr '' if no username
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            #return HttpResponseRedirect('/rec/home')
            return render_to_response('Receptionist_home.html',context,context_instance=RequestContext(request))
        else:
			context['error'] = ' wrong credentials try again'
			return render_to_response('Receptionist_login.html',context,context_instance=RequestContext(request))


    context.update(csrf(request))
    return render_to_response('Receptionist_login.html',context,context_instance=RequestContext(request))

def rec_logout(request):
    auth.logout(request)
    return HttpResponse('Successfully Logged Out')



#@login_required(login_url='/rec/login')
def home(request):
    if request.method == 'GET':
        if request.GET.get("submit_search_button"): # if search submit button clicked
            query_string = ''
            found_entries = None
            if ('q' in request.GET) and request.GET['q'].strip():
                query_string = request.GET['q']

                entry_query = get_query(query_string, ['firstname', 'lastname','patient_section','patient_room'])

                found_entries = Patient.objects.filter(entry_query)


            return render_to_response('Receptionist_home.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))

    #To Do: Handle Other parts of Receptionsit Here

    return render_to_response('Receptionist_home.html',{},context_instance=RequestContext(request))








    
