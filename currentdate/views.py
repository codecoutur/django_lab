from django.shortcuts import render
import datetime
from django.http import HttpResponse
def currentDate(request):
    current_date = datetime.datetime.now()
    resp = "<h1>current DateTime is: %s</h1>"%(current_date)
    return HttpResponse(resp)
def fourHoursAhead(request):
    fha = datetime.datetime.now()+datetime.timedelta(hours = 4)
    resp = "<h1>four hours ahead:%s</h1>"%(fha)
    return HttpResponse(resp)
def fourHoursBefore(request):
    fhb = datetime.datetime.now()+datetime.timedelta(hours = -4)
    resp = "<h1>Four hours before: %s</h1>"%(fhb)
    return HttpResponse(resp)
# Create your views here.
