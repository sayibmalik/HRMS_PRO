from django.shortcuts import render,redirect
from home.models import LeaveType,LeavesRequest,Company,Employees
from django.contrib.auth.models import User
from home.views import chklogin

# Create your views here.
def AllLeaves(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            hr = request.session['ishr']
            if hr:
                b= LeavesRequest.objects.filter(user__company=e.company)
            else:
                b = LeavesRequest.objects.filter(user=e)
            context = {"Title": "Gareeb | All Leaves", "data": b}
            return render(request, 'leaves/allleaves.html',context)
    else:
        return redirect('/app/login')

def CreateLeaveSummary(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            lt = LeaveType.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Create Leave Request", "data1": lt}
            return render(request, 'leaves/createleavesummary.html', context)
        elif request.method == 'POST':
            uid = request.session["userid"]
            emp=Employees.objects.get(user=uid)
            Desc = request.POST['desc']
            leavetype = request.POST['leavetype']
            t = LeaveType.objects.get(id=leavetype)
            frm = request.POST['leavefrom']
            to = request.POST['leaveto']
            durationdays = request.POST['durationdays']
            commentbymanager = request.POST['commentbymanager']
            status = request.POST['status']
            LeavesRequest.objects.create(user=emp,Description=Desc,Leave_Type=t,Duration_From=frm,
                                         Duration_To=to,Duration_Days=durationdays,CommentbyManager=commentbymanager,status=status)
            response = redirect('/Leaves/allleaves')
            return response
    else:
        return redirect('/app/login')


def AllocationRequest(request):
    return render(request, 'leaves/allocationrequest.html')


def LeaveDetails(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        hr = request.session['ishr']
        if hr:
            b = LeavesRequest.objects.filter(user__company=e.company)
        else:
            b = LeavesRequest.objects.filter(user=e)
        context = {"Title": "Gareeb | All Leaves", "data": b}
        return render(request, 'leaves/leavedetails.html',context)
    else:
        return redirect('/app/login')


def Leavetype(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            lt = LeaveType.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Leave Type", "data": lt}
            return render(request, 'leaves/leavetype.html', context)
    else:
        return redirect('/app/login')

def CreateLeaveType(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Gareeb | Leave Type", }
            return render(request, 'leaves/createleavetype.html',context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            title = request.POST['title']
            artitle = request.POST['artitle']
            try:
                override = request.POST['override']
                if override == "on":
                    on = True
                else:
                    on = False
            except:
                on = False
            limit = request.POST['limit']
            LeaveType.objects.create(company=e.company, Title=title,ArTitle=artitle, Override=on, Limit=limit)
            response = redirect('/Leaves/leavetype')
            return response
    else:
        return redirect('/app/login')

def LeavesToApprove(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        hr = request.session['ishr']
        if hr:
            b = LeavesRequest.objects.filter(user__company=e.company,status="Approved")
            tl = LeavesRequest.objects.filter(user__company=e.company, status="Approved")
        else:
            b = LeavesRequest.objects.filter(user=e)
        context = {"Title": "Gareeb | All Leaves", "data": b,"tl":tl.count}
        return render(request, 'leaves/leavestoapprove.html',context)
    else:
        return redirect('/app/login')


def delleave(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c = LeavesRequest.objects.get(id=pk)
            c.delete()
            return redirect("/Leaves/allleaves")
    else:
        return redirect('/app/login')

def editleave(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            lt = LeaveType.objects.filter(company=e.company)
            l = LeavesRequest.objects.get(id=pk)
            context = {"Title": "Gareeb | Create Leave Request", "data1": lt, "data":l}
            return render(request, 'leaves/createleavesummary.html', context)
        elif request.method == 'POST':
            Desc = request.POST['desc']
            leavetype = request.POST['leavetype']
            t = LeaveType.objects.get(id=leavetype)
            frm = request.POST['leavefrom']
            to = request.POST['leaveto']
            durationdays = request.POST['durationdays']
            commentbymanager = request.POST['commentbymanager']
            status = request.POST['status']
            le = LeavesRequest.objects.get(id=pk)
            le.Description = Desc
            le.Leave_Type = t
            le.Duration_From = frm
            le.Duration_To = to
            le.Duration_Days = durationdays
            le.CommentbyManager = commentbymanager
            le.status = status
            le.save()
            response = redirect('/Leaves/allleaves')
            return response
    else:
        return redirect('/app/login')