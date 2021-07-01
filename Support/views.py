from django.shortcuts import render,redirect
from home.models import Company,Employees
from .models import SupportTicket
from home.views import chklogin
import datetime
# Create your views here.

def createSupport(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            com = Employees.objects.filter(company=e.company)
            context = {"data":com}
            return render(request,"support/createticket.html")
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            ticketNumber = datetime.datetime.now().timestamp()
            subject = request.POST["subject"]
            priority = request.POST["priority"]
            description = request.POST["description"]
            SupportTicket.objects.create(company=e.company,employee=e,ticketNumber=ticketNumber,subject=subject,priority=priority,description=description)
            response = redirect('/Support/supportTickets')
            return response
    else:
        return redirect('/app/login')
    
def supportTickets(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            Ticket = SupportTicket.objects.filter(company=e.company)
            context = {"Title": "Support Tickets", "data": Ticket}
            return render(request, "support/supporttickets.html" , context)
    else:
        return redirect('/app/login')


def ticketDetails(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            T = SupportTicket.objects.get(id=pk)
            context = {"Title": "Gareeb | Create Leave Request", "data":T}
            return render(request, 'support/ticketdetails.html', context)
    else:
        return redirect('/app/login')