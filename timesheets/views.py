from django.shortcuts import render

# Create your views here.
# def Dashboard(request):
#     return render(request, 'timesheets/timesheet-dashboard.html')
#

def MyTimesheet(request):
    return render(request, 'timesheets/timesheet-dashboard.html')

def ToApprove(request):
    return render(request, 'timesheets/toapprove.html')

def Reports(request):
    return render(request, 'timesheets/reports.html')

