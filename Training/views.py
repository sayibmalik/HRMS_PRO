from django.shortcuts import render, redirect
from .models import training
from home.models import Employees
from home.views import chklogin
# Create your views here.


def Training(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            T = training.objects.filter(company=e.company)
            context = {"Title":"Training","data":T}
            return render(request , "training/training.html",context)
    else:
        return redirect('/app/login')

def Createtraining(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title":"Training"}
            return render(request , "training/createtraining.html",context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            AR_Title = request.POST["arname"]
            EN_Title = request.POST["enname"]
            AR_courceInstructions = request.POST["arCourceInstructions"]
            EN_courceInstructions = request.POST["enCourceInstructions"]
            startDate = request.POST["startdate"]
            courceDays = request.POST["couresedays"]
            website = request.POST["website"]
            numberOfSeats = request.POST["numberofseats"]
            AR_description = request.POST["arDescription"]
            EN_description = request.POST["enDescription"]
            address = request.POST["address"]
            training.objects.create(company=e.company,AR_Title=AR_Title,EN_Title=EN_Title,AR_courceInstructions=AR_courceInstructions,EN_courceInstructions=EN_courceInstructions,
                                    startDate=startDate,courceDays=courceDays,website=website,numberOfSeats=numberOfSeats,AR_description=AR_description,EN_description=EN_description,
                                    address=address)
            response = redirect('/Training/Training')
            return response
    else:
        return redirect('/app/login')

def editTraining(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            T = training.objects.get(id=pk)
            context = {"Title": "Gareeb | Create Leave Request", "data":T}
            return render(request, 'training/createtraining.html', context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            AR_Title = request.POST["arname"]
            EN_Title = request.POST["enname"]
            AR_courceInstructions = request.POST["arCourceInstructions"]
            EN_courceInstructions = request.POST["enCourceInstructions"]
            startDate = request.POST["startdate"]
            courceDays = request.POST["couresedays"]
            website = request.POST["website"]
            numberOfSeats = request.POST["numberofseats"]
            AR_description = request.POST["arDescription"]
            EN_description = request.POST["enDescription"]
            address = request.POST["address"]
            tr = training.objects.get(id=pk)
            tr.company = e.company
            tr.AR_Title = AR_Title
            tr.EN_Title = EN_Title
            tr.AR_courceInstructions = AR_courceInstructions
            tr.EN_courceInstructions = EN_courceInstructions
            tr.startDate = startDate
            tr.courceDays = courceDays
            tr.website = website
            tr.numberOfSeats = numberOfSeats
            tr.AR_description = AR_description
            tr.EN_description = EN_description
            tr.address = address
            tr.save()
            response = redirect('/Training/Training')
            return response
    else:
        return redirect('/app/login')

def trainingDetails(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            T = training.objects.get(id=pk)
            context = {"Title": "Gareeb | Create Leave Request", "data":T}
            return render(request, 'training/trainingdetails.html', context)
    else:
        return redirect('/app/login')


