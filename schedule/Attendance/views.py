from django.shortcuts import render,redirect
from home.models import Project,Employees
from  .models import Timesheet
from django.contrib.auth.models import User
from datetime import datetime
from home.views import chklogin
# Create your views here.
def Cards(request):
    return render(request, 'attendance/cards.html')

def People(request):
    return render(request, 'attendance/people.html')

def Myattendance(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            p = Project.objects.filter(company=e.company, active=True)
            t=Timesheet.objects.filter(user=uid).order_by('-id')[:1]
            if t.count() == 0:
                punchdata = ""
                punchtype = "In"
                punchedtype = ""
            else:
                if t[0].End:
                    punchdata = t[0].End
                    punchtype = "In"
                    punchedtype = "Out"
                else:
                    punchdata = t[0].Start
                    punchtype = "Out"
                    punchedtype = "In"



            context = {"Title": "HRMS | My Attendance ", "data": p, "punchdata": punchdata, "punchtype": punchtype,
                       "punchedtype": punchedtype}
            return render(request, 'attendance/employeetimesheet.html', context)
        elif request.method == "POST":
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            d = request.POST["description"]

            s=datetime.now()
            t = Timesheet.objects.filter(user=uid).order_by('-id')[:1]
            if t.count() == 0:
                try:
                    pid = request.POST["project"]
                except:
                    return redirect("/Attendance/myattendance/")
                p = Project.objects.get(id=pid)
                Timesheet.objects.create(user=u, project=p, Description=d, Start=s)
            else:
                if t[0].End:
                    try:
                        pid = request.POST["project"]
                    except:
                        return redirect("/Attendance/myattendance/")
                    p = Project.objects.get(id=pid)
                    Timesheet.objects.create(user=u, project=p, Description=d, Start=s)
                else:
                    updatetime=Timesheet.objects.get(id=t[0].id)
                    updatetime.End=datetime.now()
                    updatetime.Remarks=d
                    updatetime.save()
            return redirect("/Attendance/myattendance/")
    else:
        return redirect('/app/login')

def ManageAttendance(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            t=Timesheet.objects.filter(user=uid)
            context={"data":t}
            return render(request, 'attendance/ManageAttendence.html',context)
    else:
        return redirect('/app/login')