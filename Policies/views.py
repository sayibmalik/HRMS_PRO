from django.shortcuts import render,redirect
from home.models import Employees,Company
from home.views import chklogin
from django.core.files.storage import FileSystemStorage
from .models import policies
# Create your views here.

def ViewPolicies(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            me = policies.objects.filter(company=e.company)
            context = {"Title":"Policies","data":me}
            return render(request, "policies/viewpolicies.html",context)
    else:
        return redirect('/app/login')


def CreatePolicies(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            com = Employees.objects.filter(company=e.company)
            context = {"data": com}
            return render(request, 'policies/createpolicies.html', context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleAR = request.POST["arTitle"]
            titleEN = request.POST["enTitle"]
            fs = FileSystemStorage()
            file = request.FILES["file"]
            name = fs.save(file.name, file)
            policies.objects.create(employee=e,company=e.company,titleAR=titleAR,titleEN=titleEN,file=name)
            response = redirect('/Policies/managePolicies')
            return response
    else:
        return redirect('/app/login')

def editPolicies(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            com = Employees.objects.filter(company=e.company)
            p = policies.objects.get(id=pk)
            context = {"Title": "Memos", "Company": com, "data": p}
            return render(request, "policies/createpolicies.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleAR = request.POST["arTitle"]
            titleEN = request.POST["enTitle"]
            fs = FileSystemStorage()
            file = request.FILES["file"]
            name = fs.save(file.name, file)
            p = policies.objects.get(id=pk)
            p.employee = e
            p.company = e.company
            p.titleAR = titleAR
            p.titleEN = titleEN
            p.file = name
            p.save()
            response = redirect('/Policies/managePolicies')
            return response
    else:
        return redirect('/app/login')


def managePolicies(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            me = policies.objects.filter(company=e.company)
            context = {"Title":"Memos","data":me}
            return render(request, "policies/managepolicies.html",context)
    else:
        return redirect('/app/login')

def deletePolicies(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c = policies.objects.get(id=pk)
            c.delete()
            response = redirect('/Policies/managePolicies')
            return response
    else:
        return redirect('/app/login')