from django.shortcuts import render

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.contrib import auth
from medicine.views import *
from django.http import HttpResponse
from urllib import urlencode
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    c={'error':'','user':''}


    if request.method == "POST":
        try:
                del request.session['server_message']
        except:
                pass
        username = request.POST.get('username', '') #retunr '' if no username
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None :
          if user.get_profile().user_type==5:
            auth.login(request,user)
            c['user']=user
            #return render_to_response('medicine/list.html',c,context_instance=RequestContext(request))
            return HttpResponseRedirect(reverse('medicine_app:medicines-list'))
        else:
                c['error'] = 'wrong credentials try again'
                #return render_to_response('pharmacy/pharmacy.html',c,context_instance=RequestContext(request))
                d = {'server_message':"wrong credentials try again"}
                query_str = urlencode(d)
                request.session['server_message']='wrong credentials try again'
                return HttpResponseRedirect('/pharmacy/login/?' +query_str)


    c.update(csrf(request))
    return render_to_response('pharmacy/pharmacy.html',c,context_instance=RequestContext(request))

@csrf_exempt
def logout(request):
    auth.logout(request)
    return HttpResponse('Successfully Logged Out')




