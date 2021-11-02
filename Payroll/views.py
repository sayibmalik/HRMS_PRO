from django.shortcuts import render , redirect
from django.http import JsonResponse
from .serializers import ContractSerializer
import Employee
from home.models import EmployeePayslip,Company,Employees,SalaryRules,PayslipBatch,CreateContracts
from Attendance.models import Timesheet
from home.views import chklogin

import datetime
# Create your views here.


def employeePayslip(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        ep=EmployeePayslip.objects.filter(Employee=e.id)
        context={"data":ep}
        return render(request, 'payroll/employeepayslip.html',context)
    else:
        return redirect('/app/login')

def Editemployeepayslip(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a =EmployeePayslip.objects.get(id=pk)
            context = {"Title": "HRMS | Edit EmployeePayslip", "data": a}
        return render(request,'payroll/createemployeepayslip.html', context)
    else:
        return redirect('/app/login')



def Delemployeepayslip():
    return redirect("/Setting/companies/")


def CreateEmployeePayslip(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            q = Employees.objects.filter(company=e.company)
            p=PayslipBatch.objects.get(id=pk)
            context = {"data":q,"data2":p}
            return render(request, 'payroll/createemployeepayslip.html',context)
        elif request.method == "POST":
            emp = request.POST['emp']
            e=Employees.objects.get(id=emp)
            addition = request.POST['addition']
            resp = payrun(emp, pk)
            p=PayslipBatch.objects.get(id=pk)
            EmployeePayslip.objects.create(Employee=e,PaySlip_Name=p,addition=addition,no_of_working_hours=resp["hours"],
                                           tax=resp["tax"],other_deductions=resp["totaldeductions"],
                                           earnings_as_per_workinghours=resp["earnings"],
                                           total_earnings=resp["total_earnings"])
            return redirect("/Payroll/BatchEmployees/"+ pk+"/")
    else:
        return redirect('/app/login')


def PayslipBatches(request):
    c = chklogin(request)
    if c:
        uid=request.session["userid"]
        e= Employees.objects.get(user=uid)
        p=PayslipBatch.objects.filter(company=e.company)
        context={"data":p}
        return render(request, 'payroll/payslipbatch.html',context)
    else:
        return redirect('/app/login')


def CreatePayslipBatch(request):
    c = chklogin(request)
    if c:
        if request.method=="GET":
            return render(request, 'payroll/createpayslipbatch.html')
        elif request.method=="POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            name=request.POST["pname"]
            start=request.POST["start"]
            end=request.POST["end"]
            PayslipBatch.objects.create(company=e.company,PaySlip_Name=name,Period_From=start,Period_To=end)
            return redirect("/Payroll/payslipbatch/")
    else:
        return redirect('/app/login')

def BatchEmp(request,pk):
    c = chklogin(request)
    if c:
        p=EmployeePayslip.objects.filter(PaySlip_Name=pk)
        context={"data":pk,"data2":p}
        return render(request, 'payroll/BatchEmployees.html',context)
    else:
        return redirect('/app/login')

def salaryslip(request,pk):
    c = chklogin(request)
    if c:
        p=EmployeePayslip.objects.get(id=pk)
        e= Employees.objects.get(id=p.Employee.id)
        c=CreateContracts.objects.filter(Employee=e.id)
        salarypackage = c[0].Housing_Allowance

        context={"data":p, "employee":e,"contract":c[0],"salarypackage":salarypackage }
        return render(request, 'payroll/payslip.html',context)
    else:
        return redirect('/app/login')

def salaryStructures(request):
    return render(request, 'payroll/salarystructures.html')


def CreateSalaryStructure(request):
    return render(request, 'payroll/createsalarystructure.html')


def salaryRules(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        sr=SalaryRules.objects.filter(Company=e.company)
        context = {"data":sr}
        return render(request, 'payroll/salaryrules.html',context)
    else:
        return redirect('/app/login')


def CreateSalaryRules(request):
    c = chklogin(request)
    if c:
        if request.method=="GET":
            context = {}
            return render(request, 'payroll/createsalaryrules.html',context)
        elif request.method=="POST":
            uid= request.session["userid"]
            e = Employees.objects.get(user=uid)
            com = Company.objects.get(id=e.company.id)
            Name = request.POST['name']
            Category = request.POST['category']

            try:
                Active = request.POST['isactive']
                if Active == "on":
                    acc = True
                else:
                    acc = False
            except:
                acc= False
            Sequence = request.POST['sequence']
            try:
                AppearsOnPayslip = request.POST['AppearsOnPayslip']
                if AppearsOnPayslip == "on":
                    pay = True
                else:
                    pay = False
            except:
                pay= False
            ConditionBasedOn = request.POST['ConditionBasedOn']
            AmountType = request.POST['AmountType']
            Quantity = request.POST['Quantity']
            # FixedAmount = request.POST['']
            # Contribution_Register = request.POST['']
            SalaryRules.objects.create(Name=Name,Category=Category,Active=acc,Sequence=Sequence,
                                       AppearsOnPayslip=pay,ConditionBasedOn=ConditionBasedOn,
                                       AmountType=AmountType,Quantity=Quantity,Code="",Company=com,FixedAmount=Quantity,Contribution_Register="")
            return redirect("/Payroll/salaryrules/")
    else:
        return redirect('/app/login')


def getdata(request):
    if request.method == 'POST':
        try:
            uid = request.POST['username']
            batch = request.POST['batch']
            resp=payrun(uid,batch)
            return JsonResponse(resp, safe=False)
        except:
            resp = {'status': 'error'}
            return JsonResponse(resp, safe=False)
        resp = {'status': 'error'}
        return JsonResponse(resp, safe=False)

def payrun(uid,batch):
    e = Employees.objects.get(id=uid)
    queryset = CreateContracts.objects.filter(Employee=e.id)
    queryset = queryset[0]
    queryset2 = PayslipBatch.objects.get(id=batch)
    timeList = []
    times = Timesheet.objects.filter(Start__range=(queryset2.Period_From, queryset2.Period_To),
                                     End__range=(queryset2.Period_From, queryset2.Period_To),
                                     status=True)
    for d in times:
        ans = d.End.replace(microsecond=0) - d.Start.replace(microsecond=0)
        timeList.append(str(ans))
    print(timeList)
    totalSecs = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
    totalSecs, sec = divmod(totalSecs, 60)
    hr, min = divmod(totalSecs, 60)

    totalhours = "%d:%02d:%02d" % (hr, min, sec)
    print(totalhours)
    agregate_minutes = (hr * 60) + min
    print(agregate_minutes)
    diff = queryset2.Period_To - queryset2.Period_From
    no_of_days = int(diff.days)+1
    print(no_of_days)
    total_salary = queryset.base_salary + queryset.Housing_Allowance
    earning_by_min = total_salary / no_of_days / queryset.workinghours / 60
    print(earning_by_min)
    earnings = agregate_minutes * earning_by_min
    print(earnings)

    print(total_salary)
    tax = ((queryset.base_salary + queryset.Housing_Allowance) * queryset.GOSI / 100)
    print(tax)
    total_earnings = earnings - tax
    print(total_earnings)
    total_deduction = total_salary - total_earnings
    print(total_deduction)
    serializer = ContractSerializer(queryset, many=False)

    resp = {'status': 'valid', 'data': serializer.data, "hours": totalhours, "total_earnings": round(float(total_earnings),2),
            "totaldeductions": round(float(total_deduction),2), "tax": round(float(tax),2), "earnings": round(float(earnings),2)}
    return resp

