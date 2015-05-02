from django.http.response import HttpResponse
from django.shortcuts import render
from models import *
from django.contrib.auth.models import User
from patient.models import Patient
from django.shortcuts import render

def index(request,patient_id):
    patient=Patient.objects.get(user_id=patient_id)
    return render(request,'medical_history/medical_file.html',{'patient':patient})


def medical_history(request,patient_id):
    patient=Patient.objects.get(user_id=patient_id)
    history=patient.medical_file.get().medical_history_sheet
    return render(request,'medical_history/medical_history_sheet.html',{'patient':patient,'file':history})





def progress_notes(request,patient_id):
    patient=Patient.objects.get(user_id=patient_id)
    return render(request,'medical_history/progress_notes_sheet.html',{'patient':patient})



def physician_orders(request,patient_id):
    patient=Patient.objects.get(user_id=patient_id)
    return render(request,'medical_history/physician_oder_sheet.html',{'patient':patient})




def unit_summary(request,patient_id):
    patient=Patient.objects.get(user_id=patient_id)
    return render(request,'medical_history/unit_summary_sheet.html',{'patient':patient})