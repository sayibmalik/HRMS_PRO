from django.shortcuts import render, redirect
from home.views import chklogin
from home.models import RequestSalaryLetter
from django.contrib.auth.models import User
# Create your views here.

def requestsalaryletter(request):
    context = {"Title": "Request Salary Letter | HRMS ",}
    return render(request, 'selfservices/requestsalaryletter.html',context)

def requestleaves(request):
    context = {"Title": "Request Leaves | HRMS ",}
    return render(request, 'selfservices/requestleaves.html',context)

def requestexcuse(request):
    context = {"Title": "Request Excuse | HRMS ",}
    return render(request,'selfservices/requestexcuse.html',context)

def requestoutofoffice(request):
    context = {"Title": "Request Out Of Office | HRMS ",}
    return render(request,'selfservices/requestoutofoffice.html',context)

def requestovertime(request):
    context = {"Title": "Request Overtime | HRMS ",}
    return render(request,'selfservices/requestovertime.html',context)

def requestbusinesstrip(request):
    context = {"Title": "Request Business Trip | HRMS ",}
    return render(request,'selfservices/requestbusinesstrip.html',context)

def requesttravelticketfordependants(request):
    context = {"Title": "Request Travel Ticket For Dependants | HRMS",}
    return render(request,'selfservices/requestTravelTicketForDependants.html',context)

def requestlone(request):
    context = {"Title": "Request Lone | HRMS ",}
    return render(request,'selfservices/requestlone.html',context)

def requestgrievance(request):
    context = {"Title": "Request Grievance | HRMS",}
    return render(request,'selfservices/RequestGrievance.html',context)

def requesttraingcourse(request):
    context = {"Title": "Request Training Course | HRMS",}
    return render(request,'selfservices/requestTrainingCourse.html',context)

def pendingrequests(request):
    context = {"Title": "Pending Requests | HRMS",}
    return render(request,'selfservices/pendingrequests.html',context)

def myrequests(request):
    context = {"Title": "My Requests | HRMS",}
    return render(request,'selfservices/myrequests.html',context)

def employeerequests(request):
    context = {"Title": "Employee Requests | HRMS",}
    return render(request,'selfservices/employeerequests.html',context)