
from django.http.response import HttpResponse
from django.shortcuts import render

from models import *

def index(request):
    return HttpResponse('Welcome')