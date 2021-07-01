from django.shortcuts import render, redirect
from home.models import Project,Employees
from django.contrib.auth.models import User
from datetime import datetime
from home.views import chklogin

# Create your views here.
def retrieveproject(request):
    c = chklogin(request)
    if c:
        uid=request.session["userid"]
        e=Employees.objects.get(user=uid)
        p = Project.objects.filter(company=e.company,active=True)
        context = {"Title": "Gareeb | Project", "data": p}
        return render(request, 'project/retrieveproject.html',context)
    else:
        return redirect('/app/login')

def CreateProject(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            em = Employees.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Project", "data": em}
            return render(request, 'project/createproject.html',context)
        elif request.method == "POST":
            name = request.POST["ptitle"]
            number1 = request.POST["date1"]
            number2 = request.POST["date2"]
            prior = request.POST["prior"]
            emp = request.POST["emp"]
            em = Employees.objects.get(id=emp)
            ref = request.POST["ref"]
            des = request.POST["description"]
            Project.objects.create( Name=name, StartDate=number1, EndDate=number2,  Priority=prior,Manager=em, Reference=ref, Description=des,company=em.company)
            response = redirect('/Project/retrieveproject')
            return response
    else:
        return redirect('/app/login')


def Editproject(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            em = Employees.objects.filter(company=e.company)
            p = Project.objects.get(id=pk)
            context = {"Title": "HRMS | Edit project", "data1": p ,"data":em}
            return render(request, "project/createproject.html",context)
        elif request.method == 'POST':
            name = request.POST["ptitle"]
            sdate = request.POST["date1"]
            EndDate = request.POST["date2"]
            prior = request.POST["prior"]
            ref = request.POST["ref"]
            des = request.POST["description"]
            emp = request.POST["emp"]
            em = Employees.objects.get(id=emp)
            p = Project.objects.get(id=pk)
            p.Name = name
            p.StartDate = sdate
            p.EndDate = EndDate
            p.Priority = prior
            p.Reference = ref
            p.Description = des
            p.Manager = em
            p.save()
            response = redirect('/Project/retrieveproject')
            return response
    else:
        return redirect('/app/login')


def delproject(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            p = Project.objects.get(id=pk)
            p.delete()
            return redirect("/Project/retrieveproject/")
    else:
        return redirect('/app/login')