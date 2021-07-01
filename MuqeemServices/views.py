from django.shortcuts import render, redirect
from home.views import chklogin
from home.models import RequestSalaryLetter
from django.contrib.auth.models import User
# Create your views here.

def exitreentryvisas(request):
    context = {"Title":"Exit Re-Entry Visas | HRMS",}
    return render(request,'muqeemservices/ExitReentryVisas.html',context)

def finalexitvisas(request):
    context = {"Title":"Final Exit Visas | HRMS",}
    return render(request,'muqeemservices/FinalExitVisas.html',context)

def passportservices(request):
    context = {"Title":"Passport Services | HRMS",}
    return render(request,'muqeemservices/PassportServices.html',context)

def renewiqama(request):
    context = {"Title":"Renew Iqama | HRMS",}
    return render(request,'muqeemservices/RenewIqama.html',context)

def operationslog(request):
    context = {"Title":"Operations Log | HRMS",}
    return render(request,'muqeemservices/OperationsLog.html',context)

def issue(request):
    context = {"Title":"Issue | HRMS", }
    return render(request,'muqeemservices/Issue.html',context)

def cancel(request):
    context = {"Title":"Cancel | HRMS", }
    return render(request,'muqeemservices/Cancel.html',context)

def reprintexitreentryvisy(request):
    context = {"Title":"Reprint Exit Re-entry Visa | HRMS", }
    return render(request,'muqeemservices/ReprintExitReentryVisa.html',context)

def updatepassportinfo(request):
    context = {"Title":"Update Passport Info | HRMS",}
    return render(request,'muqeemservices/UpdatePassportInfo.html',context)

def updatepassportexpirydate(request):
    context = {"Title":"Update Passport Expiry Date | HRMS ",}
    return render(request,'muqeemservices/UpdatePassportExpiryDate.html',context)





