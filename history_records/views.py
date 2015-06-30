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
from history_records.models import *
import datetime
from django.template.loaders import filesystem
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
    user=request.user
    phys=Physician.objects.get(user=user)
    medical_files=patient.medical_file.all().filter(parent_hospital=phys.hospital).order_by('date_of_addmition')
#     if medical_files:
    
    return render(request,'medical_history/medical_files.html',{'patient':patient,'files':medical_files})
#     else:
#         return HttpResponse(request,"Salam")
#         return HttpResponseRedirect('/history/' +username+"/create_file_index")
    

def medical_file(request,username,file_id):
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
    medical_file=patient.medical_file.get(id=file_id)
    return render(request,'medical_history/medical_file.html',{'patient':patient,'file':medical_file})

def medical_history(request,username,file_id):
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
       return  edit_medical_history(request,username,file_id)
    else:
        try:
            patient=Patient.objects.get(user__username=username)
            history=patient.medical_file.get(id=file_id).medical_history_sheet

            return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'sheet':history})
        except:
            
            return HttpResponse("Currently No Records")





def progress_notes(request,username,file_id):
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
        return edit_progress_notes(request,username,file_id)
    try:
        patient=Patient.objects.get(user__username=username)
        progress_note_sheet=patient.medical_file.get(id=file_id).progress_note_sheet
        return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient,'sheet':progress_note_sheet})
    except:
        return HttpResponse("Currently No Records")



def physician_orders(request,username,file_id):
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
        return edit_physician_orders(request,username,file_id)
    try:
        patient=Patient.objects.get(user__username=username)
        orders=patient.medical_file.get(id=file_id).physician_order_sheet

        return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient,'sheet':orders})
    except:
        return HttpResponse("Currently No Records")




def unit_summary(request,username,file_id):
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
        return edit_unit_summary(request,username,file_id)
    try:
        
        patient=Patient.objects.get(user__username=username)
        unit_summary_sheet=patient.medical_file.get(id=file_id).unit_summary_sheet

        return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient,'sheet':unit_summary_sheet})
    except:
        return HttpResponse("Currently No Records")

def edit_unit_summary(request,username,file_id):

        patient=Patient.objects.get(user__username=username)
        unit_summary_sheet=patient.medical_file.get(id=file_id).unit_summary_sheet
        unit_summary_sheet.chief_complaint_and_primary_diagnosis=request.POST['ccapd']
        unit_summary_sheet.disease_progress=request.POST['dp']
        unit_summary_sheet.final_diagnosis=request.POST['fd']
        unit_summary_sheet.medical_and_surgical_procedures=request.POST['masp']
        unit_summary_sheet.patient_condition_on_discharge=request.POST['pd']
        unit_summary_sheet.recommendations_after_discharge=request.POST['ra']
        unit_summary_sheet.results_of_paraclinical_examinations=request.POST['rope']
        unit_summary_sheet.save()
        return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient,'sheet':unit_summary_sheet})




def edit_medical_history(request,username,file_id):
        patient=Patient.objects.get(user__username=username)
        history=patient.medical_file.get(id=file_id).medical_history_sheet
        history.allergy_to=request.POST['at']
        history.chief_complain=request.POST['cf']
        history.current_drug_theraphy_and_other_addiction=request.POST['crtoa']
        history.family_history=request.POST['fh']
        history.pass_diseases_history=request.POST['pdh']
        history.primary_dx=request.POST['pdx']
        history.summary=request.POST['summary']
        history.history_of_present_illness=request.POST['hopi']
        history.save()
        return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'sheet':history})



def edit_physician_orders(request,username,file_id):
        patient=Patient.objects.get(user__username=username)
        orders=patient.medical_file.get(id=file_id).physician_order_sheet
        user=request.user
        phys=Physician.objects.get(user=user)
        new_order=Order(date=request.POST['date'],time=request.POST['time'],order=request.POST['order'],physician=phys,sheet=orders)

        new_order.save()
        return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient,'sheet':orders})

def edit_progress_notes(request,username,file_id):
        patient=Patient.objects.get(user__username=username)
        progress_note_sheet=patient.medical_file.get(id=file_id).progress_note_sheet
        user=request.user
        phys=Physician.objects.get(user=user)
        new_progress_note=Progress_note(date=request.POST['date'],treatment_progress=request.POST['tp'],sheet=progress_note_sheet,physician=phys)
        new_progress_note.save()
        return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient,'sheet':progress_note_sheet})


def create_file(request,username):
    return render(request,'medical_history/create_file.html',{'username':username})

def create_medical_file(request,username):
    patient=Patient.objects.get(user__username=username)
    user=request.user
    phys=Physician.objects.get(user=user)
    if request.method=='POST':
        medi_file=MedicalFile(parent_hospital=phys.hospital,patient=patient,date_of_addmition=datetime.datetime.today().date(),open=1,ward=request.POST['ward'],room=request.POST['room'],bed=request.POST['bed'])
        medi_file.save()
        progress_sheet=Progress_notes_sheet(medical_file=medi_file,date=datetime.datetime.today().date(),attending_physician=phys)
        progress_sheet.save()
        history_sheet=Medical_history_sheet(medical_file=medi_file,attending_physician=phys)
        history_sheet.save()
        summary_sheet=Unit_summary_sheet(medical_file=medi_file,attending_physician=phys)
        summary_sheet.save()
        order_sheet=Physician_order_sheet(medical_file=medi_file,attending_physician=phys)
        order_sheet.save()
        return HttpResponseRedirect('/history/' +username)
        
    else:
        return render(request,'medical_history/medical_history_form.html')
        
