from django.shortcuts import render,redirect
from home.models import Employees,Department
from home.views import chklogin
from django.core.files.storage import FileSystemStorage
from .models import memos
# Create your views here.
def AllMemos(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            me = memos.objects.filter(company=e.company)
            context = {"Title":"Memos","data":me}
            return render(request, "memos/allmemos.html",context)
    else:
        return redirect('/app/login')


def CreateMemo(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            d = Department.objects.filter(floor__building__company=e.company)
            context = {"Title":"Memos","department":d}
            return render(request,"memos/creatememos.html",context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            department = request.POST["department"]
            d = Department.objects.get(id=department)
            notificationIcon = request.POST["notificationIcon"]
            titleAR = request.POST["arTitle"]
            titleEN = request.POST["enTitle"]
            bodyAR = request.POST["arBody"]
            bodyEN = request.POST["enBody"]
            fs = FileSystemStorage()
            file = request.FILES["file"]
            name = fs.save(file.name, file)
            memos.objects.create(employee=e,company=e.company,department=d,notificationIcon=notificationIcon,titleAR=titleAR,titleEN=titleEN,bodyAR=bodyAR,bodyEN=bodyEN,file=name)
            response = redirect('/Memos/AllMemos')
            return response
    else:
        return redirect('/app/login')

def editMemo(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            d = Department.objects.filter(floor__building__company=e.company)
            m = memos.objects.get(id=pk)
            context = {"Title":"Memos","department":d,"data":m}
            return render(request,"memos/creatememos.html",context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            department = request.POST["department"]
            d = Department.objects.get(id=department)
            notificationIcon = request.POST["notificationIcon"]
            titleAR = request.POST["arTitle"]
            titleEN = request.POST["enTitle"]
            bodyAR = request.POST["arBody"]
            bodyEN = request.POST["enBody"]
            fs = FileSystemStorage()
            file = request.FILES["file"]
            name = fs.save(file.name, file)
            me = memos.objects.get(id=pk)
            me.employee = e
            me.company = e.company
            me.department = d
            me.notificationIcon = notificationIcon
            me.titleAR = titleAR
            me.titleEN = titleEN
            me.bodyAR = bodyAR
            me.bodyEN = bodyEN
            me.file = name
            me.save()
            response = redirect('/Memos/AllMemos')
            return response
    else:
        return redirect('/app/login')

def MyMemos(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            b = memos.objects.filter(employee=e)
            context = {"Title":"Memos","data":b}
            return render(request, "memos/mymemos.html",context)
    else:
        return redirect('/app/login')

def deleteMemo(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c = memos.objects.get(id=pk)
            c.delete()
            response = redirect('/Memos/AllMemos')
            return response
    else:
        return redirect('/app/login')
