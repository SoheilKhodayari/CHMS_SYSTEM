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




def home(request):
    if not request.user.is_authenticated() or request.user.get_profile().user_type!=0:
        d = {'server_message':"Not Logged In."}
        query_str = urlencode(d)
        return HttpResponseRedirect('/login_all/?' +query_str)
    if request.method == 'GET':
        if request.GET.get("submit_search_button"): # if search submit button clicked
            query_string = ''
            found_entries = None
            if ('q' in request.GET) and request.GET['q'].strip():
                query_string = request.GET['q']

                entry_query = get_query(query_string, ['firstname', 'lastname','patient_section','patient_room'])

                found_entries = Patient.objects.filter(entry_query)


            return render_to_response('Receptionist/Receptionist_home.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))

    #To Do: Handle Other parts of Receptionsit Here

    return render_to_response('Receptionist/Receptionist_home.html',{},context_instance=RequestContext(request))








    
