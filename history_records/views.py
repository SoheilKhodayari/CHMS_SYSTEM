from django.http.response import HttpResponse
from django.shortcuts import render
from models import *
from django.contrib.auth.models import User
from patient.models import Patient
from django.shortcuts import render

def index(request,username):
    patient=Patient.objects.get(user__username=username)
    return render(request,'medical_history/medical_file.html',{'patient':patient})


def medical_history(request,username):
    try:
        patient=Patient.objects.get(user__username=username)
        history=patient.medical_file.get().medical_history_sheet
        return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'sheet':history})
    except:
        return HttpResponse("Currently No Records")





def progress_notes(request,username):
    try:
        patient=Patient.objects.get(user__username=username)
        progress_note_sheet=patient.medical_file.get().progress_note_sheet
        return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient,'sheet':progress_note_sheet})
    except:
        return HttpResponse("Currently No Records")



def physician_orders(request,username):
    try:
        patient=Patient.objects.get(user__username=username)
        orders=patient.medical_file.get().physician_order_sheet

        return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient,'sheet':orders})
    except:
        return HttpResponse("Currently No Records")




def unit_summary(request,username):
    try:
        
        patient=Patient.objects.get(user__username=username)
        unit_summary_sheet=patient.medical_file.get().unit_summary_sheet

        return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient,'sheet':unit_summary_sheet})
    except:
        return HttpResponse("Currently No Records")
