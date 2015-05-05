from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from history_records.models import *
from datetime import  datetime
from django.contrib.auth.models import User

from patient.models import *
try:
    from django.http import JsonResponse
except:
    from django.utils import simplejson
    from django.http import HttpResponse

    class JsonResponse(HttpResponse):

        def __init__(self, content, mimetype='application/json', status=None, content_type=None):
             super(JsonResponse, self).__init__(
                 content=simplejson.dumps(content),
                 mimetype=mimetype,
                 status=status,
                 content_type=content_type,
                   )

@csrf_exempt
def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user=User.objects.get(username=username)

    if user.check_password(password):
        return JsonResponse({'success':1,'type':user.profile.user_type})
    else:
        return JsonResponse({'success':0})
@csrf_exempt
def get_diagnose_file(request):


    return JsonResponse({"Saam":2})

@csrf_exempt
def get_patient_list(request):
    patients=Patient.objects.all()

    response={}
    patient_list=[]
    for patient in patients:
        medi_file=patient.medical_file.get()
        name=patient.user.first_name+' '+patient.user.last_name
        patient_list.append({'id':patient.user_id,'name':name,
                             'ward':medi_file.ward,'room':medi_file.room,'bed':medi_file.bed})
    response['response']=patient_list
    # a=  HttpResponse(response)
    # return HttpResponse(response, mimetype="application/json")
    # return HttpResponse(json.dumps(response))
    return JsonResponse(response)
    # return JsonResponse
@csrf_exempt
def get_patient_details(reuest):
    id=reuest.POST['id']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    name=patient.user.first_name+' '+patient.user.last_name
    response={'id':patient.user_id,'name':name,
                             'birthday':patient.birthday,
                             'father_name':patient.father_name,
                             'ward':medi_file.ward,
                             'room':medi_file.room,
                             'bed':medi_file.bed,
                             'add_date':medi_file.date_of_addmition}

    return JsonResponse(response)



@csrf_exempt
def get_unit_summary(request):
    id=request.POST['id']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    summary=medi_file.unit_summary_sheet
    response={'ccapd':summary.chief_complaint_and_primary_diagnosis,
              'fd':summary.final_diagnosis,
              'maps':summary.medical_and_surgical_procedures,
              'rope':summary.results_of_paraclinical_examinations,
              'dp':summary.disease_progress,
              'pd':summary.patient_condition_on_discharge,
              'ra':summary.recommendations_after_discharge,
              'dr_name':summary.attending_physician.user.first_name+summary.attending_physician.user.last_name
              }

    return JsonResponse(response)


@csrf_exempt
def get_physician_order(request):
    id=request.POST['id']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    orders_sheet=medi_file.physician_order_sheet
    orders=orders_sheet.orders.all()
    orders_list=[]
    for ord in orders:
        name=ord.physician.user.first_name+' '+ord.physician.user.last_name
        orders_list.append({'date':ord.date,
                            'time':ord.time,
                            'order':ord.order,
                            'dr_name':name})
    response={'orders':orders_list}

    return JsonResponse(response)


@csrf_exempt
def set_physician_order(request):
    id=request.POST['id']
    time=request.POST['time']
    date=request.POST['date']
    user_id=request.POST['user_id']
    physician=Physician.objects.get(user_id=user_id)
    description=request.POST['description']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    orders_sheet=medi_file.physician_order_sheet
    try:
        new_order=Order(date=date,time=time,order=description,physician=physician,sheet=orders_sheet)
        new_order.save()
        orders_sheet.orders.add(new_order)
        return JsonResponse({'success':1})
    except:
        return JsonResponse({'success':0})


@csrf_exempt
def get_progress_note(request):
    id=request.POST['id']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    prog_note=medi_file.progress_note_sheet
    notes=prog_note.notes.all()
    notes_list=[]
    for note in notes:
        name=note.physician.user.first_name+' '+note.physician.user.last_name
        notes_list.append({'date':note.date,'treatment_progress':note.treatment_progress,'dr_name':name})
    response={'notes':notes_list}
    return JsonResponse(response)





@csrf_exempt
def set_progress_note(request):
    id=request.POST['id']
    date=request.POST['date']
    user_id=request.POST['user_id']
    physician=Physician.objects.get(user_id=user_id)
    note=request.POST['description']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    prog_note=medi_file.progress_note_sheet
    treatment_note=Progress_note(date=date,treatment_progress=note,physician=physician,sheet=prog_note)
    treatment_note.save()
    prog_note.notes.add(treatment_note)

    return JsonResponse({'success':1})

@csrf_exempt
def get_medical_history(request):
    id=request.POST['id']
    patient=Patient.objects.get(user_id=id)
    medi_file=patient.medical_file.get()
    history=medi_file.medical_history_sheet
    name=history.attending_physician.user.first_name+' '+history.attending_physician.user.last_name
    response={'cf':history.chief_complain,'hopi':history.history_of_present_illness,'pdh':history.pass_diseases_history,
              'crtoa':history.current_drug_theraphy_and_other_addiction,'at':history.allergy_to,
              'fh':history.family_history,
              'summary':history.summary,'pxd':history.primary_dx,
              'dr_name':name
              }


    return JsonResponse(response)


@csrf_exempt
def get_physician_details(request):
    id=request.POST['dr_id']
    physician=Physician.objects.get(user_id=id)
    response={'name':physician.user.first_name+physician.user.last_name,'speciality':physician.specialty}
    return JsonResponse(response)

