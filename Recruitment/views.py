from django.shortcuts import render, redirect
from home.models import Company,Employees
from django.contrib.auth.models import User
from .models import Jobs, Resumes
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from home.views import chklogin


# Create your views here.
def Recruitment(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            r = Jobs.objects.filter(company=e.company)
            context = {"Title": "Gareeb | HRMS", "data": r}
            return render(request, 'recruitment/recruitment.html', context)
        elif request.method == 'POST':
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            e = Employees.objects.get(user=u)
            c = Company.objects.get(id=e.company.id)
            title = request.POST['title']
            Description = request.POST['desc']
            Jobs.objects.create(user=u, company=c, title=title, Description=Description)
            return redirect('/Recruitment/recruitment/')
    else:
        return redirect('/app/login')


def Applyjob(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            j = Jobs.objects.get(id=pk)
            r = Resumes.objects.filter(job=j)
            context = {"Title": "Gareeb | HRMS", "data": j, "data1": r}
            return render(request, 'recruitment/applyjob.html', context)
        elif request.method == "POST":
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            fs = FileSystemStorage()
            cv = request.FILES["resume"]
            name = fs.save(cv.name, cv)
            job = Jobs.objects.get(id=pk)
            n = Resumes.objects.create(job=job, user=u, CV=name)
            return redirect('/Recruitment/applyjob/' + pk)
    else:
        return redirect('/app/login')

def deljob(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c = Jobs.objects.get(id=pk)
            c.delete()
            return redirect("/Recruitment/recruitment/")
    else:
        return redirect('/app/login')



def editrecruitment(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            r = Jobs.objects.get(id=pk)
            context = {"r":r}
            return render(request,"recruitment/recruitment.html",context)
        elif request.method == "POST":
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            e = Employees.objects.get(user=u)
            c = Company.objects.get(id=e.company.id)
            ti = request.POST['title']
            Desc = request.POST['desc']
            r = Jobs.objects.get(id=pk)
            r.user =u
            r.company = c
            r.title = ti
            r.Description = Desc
            r.save()
            response = redirect('/Recruitment/recruitment/')
            return response
    else:
        return redirect('/app/login')