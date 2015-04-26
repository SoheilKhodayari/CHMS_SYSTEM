from django.http.response import HttpResponse
from django.shortcuts import render
from models import *
from django.contrib.auth.models import User

def index(request):
    user=request.user
    histoty=user.patient.history
    context={
        'history':histoty
    }

    return render(request,'medical_history/show.html',{'user':user})

