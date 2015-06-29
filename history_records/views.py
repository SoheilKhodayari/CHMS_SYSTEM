from django.http.response import HttpResponse
from django.shortcuts import render
from models import *
from django.contrib.auth.models import User
from patient.models import Patient
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from urllib import  urlencode
from django.http.response import HttpResponseRedirect
from physician.models import *


def index(request,username):
    try:
       if not (request.user.is_authenticated() and (request.user.profile.user_type==6 or request.user.profile.user_type==0)):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    patient=Patient.objects.get(user__username=username)
    return render(request,'medical_history/medical_file.html',{'patient':patient})


def medical_history(request,username):
    try:
        if not (request.user.is_authenticated() and (request.user.profile.user_type==6 or request.user.profile.user_type==0)):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    if not (request.user.profile.user_type==6 or request.user.profile.user_type==0 ):
        return HttpResponse('access denied')
    if request.method=="POST":
       return  edit_medical_history(request,username)
    else:
        try:
            patient=Patient.objects.get(user__username=username)
            history=patient.medical_file.get().medical_history_sheet

            return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'sheet':history})
        except:
            return HttpResponse("Currently No Records")





def progress_notes(request,username):
    try:
       if not (request.user.is_authenticated() and (request.user.profile.user_type==6 or request.user.profile.user_type==0)):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    if not (request.user.profile.user_type==6 or request.user.profile.user_type==0):
        return HttpResponse('access denied')
    if request.method=="POST":
        return edit_progress_notes(request,username)
    try:
        patient=Patient.objects.get(user__username=username)
        progress_note_sheet=patient.medical_file.get().progress_note_sheet
        return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient,'sheet':progress_note_sheet})
    except:
        return HttpResponse("Currently No Records")



def physician_orders(request,username):
    try:
       if not (request.user.is_authenticated() and (request.user.profile.user_type==6 or request.user.profile.user_type==0)):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    if not (request.user.profile.user_type==6 or request.user.profile.user_type==0) :
        return HttpResponse('access denied')
    if request.method=="POST":
        return edit_physician_orders(request,username)
    try:
        patient=Patient.objects.get(user__username=username)
        orders=patient.medical_file.get().physician_order_sheet

        return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient,'sheet':orders})
    except:
        return HttpResponse("Currently No Records")




def unit_summary(request,username):
    try:
       if not (request.user.is_authenticated() and (request.user.profile.user_type==6 or request.user.profile.user_type==0)):
           d = {'server_message':"Not Logged In."}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    except:
           d = {'server_message':"not logged in"}
           query_str = urlencode(d)
           return HttpResponseRedirect('/login_all/?' +query_str)
    if not (request.user.profile.user_type==6 or request.user.profile.user_type==0):
        return HttpResponse('access denied')
    if request.method=="POST":
        return edit_unit_summary(request,username)
    try:
        
        patient=Patient.objects.get(user__username=username)
        unit_summary_sheet=patient.medical_file.get().unit_summary_sheet

        return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient,'sheet':unit_summary_sheet})
    except:
        return HttpResponse("Currently No Records")

def edit_unit_summary(request,username):

        patient=Patient.objects.get(user__username=username)
        unit_summary_sheet=patient.medical_file.get().unit_summary_sheet
        unit_summary_sheet.chief_complaint_and_primary_diagnosis=request.POST['ccapd']
        unit_summary_sheet.disease_progress=request.POST['dp']
        unit_summary_sheet.final_diagnosis=request.POST['fd']
        unit_summary_sheet.medical_and_surgical_procedures=request.POST['masp']
        unit_summary_sheet.patient_condition_on_discharge=request.POST['pd']
        unit_summary_sheet.recommendations_after_discharge=request.POST['ra']
        unit_summary_sheet.results_of_paraclinical_examinations=request.POST['rope']
        unit_summary_sheet.save()
        return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient,'sheet':unit_summary_sheet})




def edit_medical_history(request,username):
        patient=Patient.objects.get(user__username=username)
        history=patient.medical_file.get().medical_history_sheet
        history.allergy_to=request.POST['at']
        history.chief_complain=request.POST['cf']
        history.current_drug_theraphy_and_other_addiction=request.POST['crtoa']
        history.family_history=request.POST['fh']
        history.pass_diseases_history=request.POST['pdh']
        history.primary_dx=request.POST['pdx']
        history.summary=request.POST['summary']
        history.history_of_present_illness=request.POST['hopi']
        return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'sheet':history})



def edit_physician_orders(request,username):
        patient=Patient.objects.get(user__username=username)
        orders=patient.medical_file.get().physician_order_sheet
        user=request.user
        phys=Physician.objects.get(user=user)
        new_order=Order(date=request.POST['date'],time=request.POST['time'],order=request.POST['order'],physician=phys,sheet=orders)

        new_order.save()
        return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient,'sheet':orders})

def edit_progress_notes(request,username):
        patient=Patient.objects.get(user__username=username)
        progress_note_sheet=patient.medical_file.get().progress_note_sheet
        user=request.user
        phys=Physician.objects.get(user=user)
        new_progress_note=Progress_note(date=request.POST['date'],treatment_progress=request.POST['tp'],sheet=progress_note_sheet,physician=phys)
        new_progress_note.save()
        return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient,'sheet':progress_note_sheet})

