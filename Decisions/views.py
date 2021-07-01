from django.shortcuts import render, redirect
from home.views import chklogin
from home.models import RequestSalaryLetter
from django.contrib.auth.models import User
# Create your views here.

def endofserviceforemployee(request):
    context = {"Title": "End of service for Employee | HRMS ",}
    return render(request,'decisions/EndofserviceforEmployee.html',context)

def suspendemployeesalary(request):
    context = {"Title": "Suspend Employee Salary | HRMS ", }
    return render(request, 'decisions/SuspendEmployeeSalary.html', context)

def transferemployeedecision(request):
    context = {"Title": "Transfer Employee Decision | HRMS ", }
    return render(request, 'decisions/TransferEmployeeDecision.html', context)

def pendingdecision(request):
    context = {"Title": "Pending Decision | HRMS ", }
    return render(request, 'decisions/PendingDecision.html', context)

def mydecisions(request):
    context = {"Title": "My Decisions | HRMS ", }
    return render(request, 'decisions/MyDecisions.html', context)

def alldecision(request):
    context = {"Title": "All Decision | HRMS ", }
    return render(request, 'decisions/AllDecision.html', context)

