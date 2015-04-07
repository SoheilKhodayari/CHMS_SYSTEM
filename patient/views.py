import datetime

from django.http.response import HttpResponse
from django.shortcuts import render

from models import *


def index(request):
    return render(request , 'patient/register.html')
    




def register(request):
    
    
    
    
#     username=request.POST['username']
#     first_name=request.POST['first_name']
#     last_name=request.POST['last_name']
#     email=request.POST['email']
#     Tel=request.POST['tel']
#     ssn=request.POST['ssn']
    b_day=request.POST['day']
    b_month=request.POST['month']
    b_year=request.POST['year']
    birth=datetime.datetime(b_year,b_month,b_day);
#     age=request.POST['age']
#     marital_status=request.POST['marital_status']
#     marital_status_notes=request.POST['marital_status_notes']
#     occupation=request.POST['occupation']
#     occupation_notes=request.POST['occupation_notes']
#     country=request.POST['country']
#     city=request.POST['city']
#     district=request.POST['district']
#     street=request.POST['street']
#     alley=request.POST['alley']
#     building_no=request.POST['building_no']
#     postal_code=request.POST['postal_code']
    
    patient=Patient(
                        username=request.POST['username'],
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                        email=request.POST['email'],
                        Tel=request.POST['tel'],
                        ssn=request.POST['ssn'],
                        birthday=birth,
                        age=request.POST['age'],
                        marital_status=request.POST['marital_status'],
                        marital_status_notes=request.POST['marital_status_notes'],
                        occupation=request.POST['occupation'],
                        occupation_notes=request.POST['occupation_notes'],
                        country=request.POST['country'],
                        city=request.POST['city'],
                        district=request.POST['district'],
                        street=request.POST['street'],
                        alley=request.POST['alley'],
                        building_no=request.POST['building_no'],
                        postal_code=request.POST['postal_code']
                    
                    )
    
    
    









