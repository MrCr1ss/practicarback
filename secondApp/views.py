from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Fecha y Hora actual: </b>"+str(dt)
    return HttpResponse(s)
