from django.shortcuts import render, redirect
from home.models import LeaveType, LeavesRequest, Company, Employees, JobTitle, bank, EmployementGrades, \
    EmployementLevel, allowances, deductionAddition \
    , Floor, Department, ContractType, insurance, holidays, costcenter, location, documentType, custodytype, brands, \
    brandModel
from django.contrib.auth.models import User
from home.views import chklogin
import datetime


# Create your views here.

def conf(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/company.html", context)
    else:
        return redirect('/app/login')


def newLeavetype(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            leavet = LeaveType.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Leave Type", "lev": leavet}
            return render(request, 'company/leavetype.html', context)
    else:
        return redirect('/app/login')


def newCreateLeaveType(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Gareeb | Leave Type", }
            return render(request, 'company/createleavetype.html', context)
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
            LeaveType.objects.create(company=e.company, Title=title, ArTitle=artitle, Override=on, Limit=limit)
            response = redirect('/conf/newLeavetype')
            return response
    else:
        return redirect('/app/login')


def editLeaveType(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            lt = LeaveType.objects.get(id=pk)
            context = {"Title": "Gareeb | Leave Type", "leavetype": lt}
            return render(request, 'company/createleavetype.html', context)
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
            l = LeaveType.objects.get(id=pk)
            l.company = e.company
            l.Title = title
            l.Override = on
            l.Limit = limit
            l.ArTitle = artitle
            l.save()
            response = redirect('/conf/newLeavetype')
            return response
    else:
        return redirect('/app/login')


def delleavetype(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            l = LeaveType.objects.get(id=pk)
            l.delete()
            response = redirect('/conf/newLeavetype')
            return response
    else:
        return redirect('/app/login')


def jobtitle(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            emp = Employees.objects.get(user=uid)
            jobt = JobTitle.objects.filter(company=emp.company)
            context = {"Title": "Company", "job": jobt}
            return render(request, "company/jobtitle.html", context)
    else:
        return redirect('/app/login')


def createjobtitle(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Job Title"}
            return render(request, "company/createjobtitle.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            jobtitleEn = request.POST["jobtitleEn"]
            jobtitleAr = request.POST["jobtitleAr"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            JobTitle.objects.create(company=e.company, jobtitleEn=jobtitleEn, jobtitleAr=jobtitleAr, desEn=desEn,
                                    desAr=desAr)
            response = redirect('/conf/jobtitle')
            return response
    else:
        return redirect('/app/login')


def editjobtitle(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            jobtitle = JobTitle.objects.get(id=pk)
            context = {"Title": "Create Job Title", "jb": jobtitle}
            return render(request, "company/createjobtitle.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            jobtitleEn = request.POST["jobtitleEn"]
            jobtitleAr = request.POST["jobtitleAr"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            jt = JobTitle.objects.get(id=pk)
            jt.jobtitleEn = jobtitleEn
            jt.jobtitleAr = jobtitleAr
            jt.desEn = desEn
            jt.desAr = desAr
            jt.company = e.company
            jt.save()
            response = redirect('/conf/jobtitle')
            return response
    else:
        return redirect('/app/login')


def deljobtitle(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            l = JobTitle.objects.get(id=pk)
            l.delete()
            return redirect('/conf/jobtitle')
    else:
        return redirect('/app/login')


def employementgrades(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            emp = Employees.objects.get(user=uid)
            empgrades = EmployementGrades.objects.filter(company=emp.company)
            context = {"Title": "Company", "empgrades": empgrades}
            return render(request, "company/employementgrades.html", context)
    else:
        return redirect('/app/login')


def createemployementgrades(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/createemployementgrades.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            EmployementGrades.objects.create(company=e.company, titleEn=titleEn, titleAr=titleAr, desEn=desEn,
                                             desAr=desAr)
            return redirect("/conf/employementgrades")
    else:
        return redirect('/app/login')


def editemployementgrades(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            editemployementgrade = EmployementGrades.objects.get(id=pk)
            context = {"Title": "Company", "data": editemployementgrade}
            return render(request, "company/createemployementgrades.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            grade = EmployementGrades.objects.get(id=pk)
            grade.company = e.company
            grade.titleEn = titleEn
            grade.titleAr = titleAr
            grade.desEn = desEn
            grade.desAr = desAr
            grade.save()
            return redirect("/conf/employementgrades")
    else:
        return redirect('/app/login')


def delemployementgrade(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            e = EmployementGrades.objects.get(id=pk)
            e.delete()
            response = redirect('/conf/employementgrades')
            return response
    else:
        return redirect('/app/login')


def employementlevel(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            level = EmployementLevel.objects.filter(company=e.company)
            context = {"Title": "Company", "level": level}
            return render(request, "company/employementlevel.html", context)
    else:
        return redirect('/app/login')


def createemployementlevel(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/createemployementlevel.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            EmployementLevel.objects.create(company=e.company, titleEn=titleEn, titleAr=titleAr, desEn=desEn,
                                            desAr=desAr)
            return redirect("/conf/employementlevel")
    else:
        return redirect('/app/login')


def editemployementlevel(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            level = EmployementLevel.objects.get(id=pk)
            context = {"Title": "Company", "data": level}
            return render(request, "company/createemployementlevel.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            level = EmployementLevel.objects.get(id=pk)
            level.company = e.company
            level.titleEn = titleEn
            level.titleAr = titleAr
            level.desEn = desEn
            level.desAr = desAr
            level.save()
            return redirect("/conf/employementlevel")
    else:
        return redirect('/app/login')


def delemployementlevel(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            e = EmployementLevel.objects.get(id=pk)
            e.delete()
            response = redirect('/conf/employementlevel')
            return response
    else:
        return redirect('/app/login')


def workshift(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/workshift.html", context)
    else:
        return redirect('/app/login')


def createworkshift(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/createworkshift.html", context)
    else:
        return redirect('/app/login')


def allowance(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            allow = allowances.objects.filter(company=e.company)
            context = {"Title": "Company", "allowance": allow}
            return render(request, "company/allowance.html", context)
    else:
        return redirect('/app/login')


def createallowance(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/createallowance.html", context)
        elif request.method == "POST":
            operationType = request.POST["Operation"]
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            valueType = request.POST["valueType"]
            value = request.POST["value"]
            maxValue = request.POST["maxValue"]
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            allowances.objects.create(company=e.company, operationType=operationType, arName=arName, enName=enName,
                                      valueType=valueType, value=value, maxValue=maxValue)
            return redirect("/conf/allowance")
    else:
        return redirect('/app/login')


def editallowance(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            allow = allowances.objects.get(id=pk)
            context = {"Title": "Company", "allowance": allow}
            return render(request, "company/createallowance.html", context)
        elif request.method == "POST":
            operationType = request.POST["Operation"]
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            valueType = request.POST["valueType"]
            value = request.POST["value"]
            maxValue = request.POST["maxValue"]
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            a = allowances.objects.get(id=pk)
            a.operationType = operationType
            a.arName = arName
            a.enName = enName
            a.valueType = valueType
            a.value = value
            a.maxValue = maxValue
            a.company = e.company
            a.save()
            return redirect("/conf/allowance")
    else:
        return redirect('/app/login')


def delallowance(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            e = allowances.objects.get(id=pk)
            e.delete()
            response = redirect('/conf/allowance')
            return response
    else:
        return redirect('/app/login')


def deduction(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            da = deductionAddition.objects.filter(company=e.company)
            context = {"Title": "Company", "data": da}
            return render(request, "company/deduction.html", context)
    else:
        return redirect('/app/login')


def creatededuction(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/creatededuction.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            opeartionType = request.POST["opeartionType"]
            deductionAddition.objects.create(company=e.company, arName=arName, enName=enName,
                                             opeartionType=opeartionType)
            return redirect("/conf/deduction")
    else:
        return redirect('/app/login')


def editdeduction(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            da = deductionAddition.objects.get(id=pk)
            context = {"Title": "Company", "da": da}
            return render(request, "company/creatededuction.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            opeartionType = request.POST["opeartionType"]
            d = deductionAddition.objects.get(id=pk)
            d.company = e.company
            d.arName = arName
            d.enName = enName
            d.opeartionType = opeartionType
            d.save()
            return redirect("/conf/deduction")
    else:
        return redirect('/app/login')


def deldeduction(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            e = deductionAddition.objects.get(id=pk)
            e.delete()
            response = redirect('/conf/deduction')
            return response
    else:
        return redirect('/app/login')


def payroll(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/payroll.html", context)
    else:
        return redirect('/app/login')


def createpayroll(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/createpayroll.html", context)
    else:
        return redirect('/app/login')


def payrolltemplate(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/payrolltemplate.html", context)
    else:
        return redirect('/app/login')


def createpayrolltemplate(request):
    c = chklogin(request)
    if c:
        context = {"Title": "Company"}
        return render(request, "company/createpayrolltemplate.html", context)
    else:
        return redirect('/app/login')


def banks(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            bnk = bank.objects.filter(company=e.company)
            context = {"Title": "Company", "data": bnk}
            return render(request, "company/banks.html", context)
    else:
        return redirect('/app/login')


def createbanks(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/createbanks.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            transferFees = request.POST["transferFees"]
            bank.objects.create(company=e.company, arName=arName, enName=enName, transferFees=transferFees)
            return redirect("/conf/banks")
    else:
        return redirect('/app/login')


def editbank(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            bnk = bank.objects.get(id=pk)
            context = {"Title": "Company", "data": bnk}
            return render(request, "company/createbanks.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            transferFees = request.POST["transferFees"]
            b = bank.objects.get(id=pk)
            b.company = e.company
            b.arName = arName
            b.enName = enName
            b.transferFees = transferFees
            b.save()
            return redirect("/conf/banks")
    else:
        return redirect('/app/login')


def delbank(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST['id']
            b = bank.objects.get(id=pk)
            b.delete()
            response = redirect('/conf/banks')
            return response
    else:
        return redirect('/app/login')


def newdepartments(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = Employees.objects.get(user=uid)
        p = Department.objects.filter(floor__building__company=u.company)
        context = {"Title": "Gareeb | Setting", "data": p}
        return render(request, 'company/departments.html', context)
    else:
        return redirect('/app/login')


def newCreateDepartments(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            u = Employees.objects.get(user=uid)
            c = Floor.objects.filter(building__company=u.company)
            context = {"Title": "Gareeb | Setting", "data": c}
            return render(request, 'company/createdepartments.html', context)
        elif request.method == "POST":
            title = request.POST["title"]
            titleAr = request.POST["titleAr"]
            belong = request.POST["belong"]
            floor = request.POST["floor"]
            f = Floor.objects.get(id=floor)
            Department.objects.create(title=title, floor=f, titalAR=titleAr, belong=belong)
            response = redirect('/conf/newdepartments')
            return response
    else:
        return redirect('/app/login')


def newEditdepartment(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            u = Employees.objects.get(user=uid)
            c = Floor.objects.filter(building__company=u.company)
            p = Department.objects.get(id=pk)
            context = {"Title": "HRMS | Edit Department", "data2": p, "data": c}
            return render(request, "company/createdepartments.html", context)
        elif request.method == 'POST':
            title = request.POST["title"]
            titleAr = request.POST["titleAr"]
            belong = request.POST["belong"]
            floor = request.POST["floor"]
            f = Floor.objects.get(id=floor)
            p = Department.objects.get(id=pk)
            p.title = title
            p.titleAR = titleAr
            p.belong = belong
            p.floor = f
            p.save()
            response = redirect('/conf/newdepartments')
            return response
    else:
        return redirect('/app/login')


def newdeldepartment(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["department_id"]
            p = Department.objects.get(id=pk)
            p.delete()
            return redirect("/conf/newdepartments/")
    else:
        return redirect('/app/login')


def newcontracts(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = Employees.objects.get(user=uid)
        c = ContractType.objects.filter(company=u.company)
        context = {"Title": "Gareeb | Contracts", "data": c}
        return render(request, 'company/contracts.html', context)
    else:
        return redirect('/app/login')


def newcreatecontracts(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/createccontracts.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            title = request.POST["title"]
            titleAr = request.POST["titleAr"]
            CompanyGOSIForSaudi = request.POST["CompanyGOSIForSaudi"]
            CompanyGOSIForNonSaudi = request.POST["CompanyGOSIForNonSaudi"]
            ContractType.objects.create(company=e.company, title=title, titleAr=titleAr,
                                        CompanyGOSIForSaudi=CompanyGOSIForSaudi,
                                        CompanyGOSIForNonSaudi=CompanyGOSIForNonSaudi)
            return redirect("/conf/newcontracts")
    else:
        return redirect('/app/login')


def editnewcontract(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            c = ContractType.objects.get(id=pk)
            context = {"Title": "Create Contracts", "data": c}
            return render(request, "company/createccontracts.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            title = request.POST["title"]
            titleAr = request.POST["titleAr"]
            CompanyGOSIForSaudi = request.POST["CompanyGOSIForSaudi"]
            CompanyGOSIForNonSaudi = request.POST["CompanyGOSIForNonSaudi"]
            c = ContractType.objects.get(id=pk)
            c.company = e.company
            c.title = title
            c.titleAr = titleAr
            c.CompanyGOSIForSaudi = CompanyGOSIForSaudi
            c.CompanyGOSIForNonSaudi = CompanyGOSIForNonSaudi
            c.save()
            return redirect("/conf/newcontracts")
    else:
        return redirect('/app/login')


def editnewcontractform(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/editnewcontractform.html", context)
    else:
        return redirect('/app/login')


def delnewcontract(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            cont = ContractType.objects.get(id=pk)
            cont.delete()
            return redirect("/conf/newcontracts")
    else:
        return redirect('/app/login')


def insurances(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            i = insurance.objects.filter(company=e.company)
            context = {"Title": "Company", "data": i}
            return render(request, "company/insurance.html", context)
    else:
        return redirect('/app/login')


def createinsurance(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Company"}
            return render(request, "company/createinsurance.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            insurance.objects.create(company=e.company, titleEn=titleEn, titleAr=titleAr, desEn=desEn, desAr=desAr)
            return redirect("/conf/insurances")
    else:
        return redirect('/app/login')


def editinsurance(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            ins = insurance.objects.get(id=pk)
            context = {"Title": "Company", "data": ins}
            return render(request, "company/createinsurance.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            i = insurance.objects.get(id=pk)
            i.company = e.company
            i.titleEn = titleEn
            i.titleAr = titleAr
            i.desEn = desEn
            i.desAr = desAr
            i.save()
            return redirect("/conf/insurances")
    else:
        return redirect('/app/login')


def delinsurance(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            i = insurance.objects.get(id=pk)
            i.delete()
            return redirect('/conf/insurances')
    else:
        return redirect('/app/login')


def holiday(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            hold = holidays.objects.filter(company=e.company)
            context = {"Title": "Create Contracts", "data": hold}
            return render(request, "company/holidays.html", context)
    else:
        return redirect('/app/login')


def createholidays(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/createholidays.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            nameAR = request.POST["nameAR"]
            nameEN = request.POST["nameEN"]
            fromDate = request.POST["fromDate"]
            toDate = request.POST["toDate"]
            holidays.objects.create(company=e.company, nameAR=nameAR, nameEN=nameEN, fromDate=fromDate, toDate=toDate)
            return redirect("/conf/holiday")
    else:
        return redirect('/app/login')


def editHolidays(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            h = holidays.objects.get(id=pk)
            context = {"Title": "Edit Holidays", "data": h}
            return render(request, "company/createholidays.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            nameAR = request.POST["nameAR"]
            nameEN = request.POST["nameEN"]
            fromDate = request.POST["fromDate"]
            toDate = request.POST["toDate"]
            h = holidays.objects.get(id=pk)
            h.company = e.company
            h.nameAR = nameAR
            h.nameEn = nameEN
            h.fromDate = fromDate
            h.toDate = toDate
            h.save()
            return redirect("/conf/holiday")
    else:
        return redirect('/app/login')


def delHolidays(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            h = holidays.objects.get(id=pk)
            h.delete()
            return redirect("/conf/holiday")
    else:
        return redirect('/app/login')


def costcenters(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            cc = costcenter.objects.filter(company=e.company)
            context = {"Title": "Create Contracts", "data": cc}
            return render(request, "company/costcenters.html", context)
    else:
        return redirect('/app/login')


def createcostcenters(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/createcostcenters.html", context)
        elif request.method == "POST":
            nameAR = request.POST["nameAR"]
            nameEN = request.POST["nameEN"]
            desAR = request.POST["desAR"]
            desEN = request.POST["desEN"]
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            costcenter.objects.create(nameAR=nameAR, nameEN=nameEN, desAR=desAR, desEN=desEN, company=e.company)
            return redirect("/conf/costcenters")
    else:
        return redirect('/app/login')


def editcostcenter(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            cc = costcenter.objects.get(id=pk)
            context = {"Title": "Edit Cost Center", "data": cc}
            return render(request, "company/createcostcenters.html", context)
        elif request.method == "POST":
            nameAR = request.POST["nameAR"]
            nameEN = request.POST["nameEN"]
            desAR = request.POST["desAR"]
            desEN = request.POST["desEN"]
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            cc = costcenter.objects.get(id=pk)
            cc.nameAR = nameAR
            cc.nameEN = nameEN
            cc.desAR = desAR
            cc.desEN = desEN
            cc.company = e.company
            cc.save()
            return redirect("/conf/costcenters")
    else:
        return redirect('/app/login')


def delcostcenter(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            cc = costcenter.objects.get(id=pk)
            cc.delete()
            return redirect("/conf/costcenters")
    else:
        return redirect('/app/login')


def locations(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            l = location.objects.filter(company=e.company)
            context = {"Title": "Create Contracts", "data": l}
            return render(request, "company/locations.html", context)
    else:
        return redirect('/app/login')


def createlocation(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/createlocation.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            locationnameAR = request.POST["locationnameAR"]
            locationnameEN = request.POST["locationnameEN"]
            country = request.POST["country"]
            cityAR = request.POST["cityAR"]
            cityEN = request.POST["cityEN"]
            streetAR = request.POST["streetAR"]
            streetEN = request.POST["streetEN"]
            stateAR = request.POST["stateAR"]
            stateEN = request.POST["stateEN"]
            telephone = request.POST["telephone"]
            postalCode = request.POST["postalCode"]
            location.objects.create(locationnameAR=locationnameAR, locationnameEN=locationnameEN, country=country,
                                    cityAR=cityAR, cityEN=cityEN, streetAR=streetAR, streetEN=streetEN,
                                    stateAR=stateAR, stateEN=stateEN, telephone=telephone, postalCode=postalCode,
                                    company=e.company)
            return redirect("/conf/locations")
    else:
        return redirect('/app/login')


def editLocation(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            l = location.objects.get(id=pk)
            context = {"Title": "Create Contracts", "data": l}
            return render(request, "company/createlocation.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            locationnameAR = request.POST["locationnameAR"]
            locationnameEN = request.POST["locationnameEN"]
            country = request.POST["country"]
            cityAR = request.POST["cityAR"]
            cityEN = request.POST["cityEN"]
            streetAR = request.POST["streetAR"]
            streetEN = request.POST["streetEN"]
            stateAR = request.POST["stateAR"]
            stateEN = request.POST["stateEN"]
            telephone = request.POST["telephone"]
            postalCode = request.POST["postalCode"]
            l = location.objects.get(id=pk)
            l.locationnameAR = locationnameAR
            l.locationnameEN = locationnameEN
            l.country = country
            l.cityAR = cityAR
            l.cityEN = cityEN
            l.streetAR = streetAR
            l.streetEN = streetEN
            l.stateAR = stateAR
            l.stateEN = stateEN
            l.telephone = telephone
            l.postalCode = postalCode
            l.company = e.company
            l.save()
            return redirect("/conf/locations")
    else:
        return redirect('/app/login')


def dellocation(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            l = location.objects.get(id=pk)
            l.delete()
            return redirect("/conf/locations")
    else:
        return redirect('/app/login')


def documenttypes(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            d = documentType.objects.filter(company=e.company)
            context = {"Title": "Create Contracts", "data": d}
            return render(request, "company/documenttypes.html", context)
    else:
        return redirect('/app/login')


def createdocumenttype(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Contracts"}
            return render(request, "company/createdocumenttype.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            documentType.objects.create(company=e.company, titleEn=titleEn, titleAr=titleAr, desEn=desEn, desAr=desAr)
            return redirect("/conf/documenttypes")
    else:
        return redirect('/app/login')


def editdocumenttype(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            d = documentType.objects.get(id=pk)
            context = {"Title": "Company", "data": d}
            return render(request, "company/createdocumenttype.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            titleEn = request.POST["titleEN"]
            titleAr = request.POST["titleAR"]
            desEn = request.POST["desEN"]
            desAr = request.POST["desAR"]
            d = documentType.objects.get(id=pk)
            d.company = e.company
            d.titleEn = titleEn
            d.titleAr = titleAr
            d.desEn = desEn
            d.desAr = desAr
            d.save()
            return redirect("/conf/documenttypes")
    else:
        return redirect('/app/login')


def deldocumenttype(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            d = documentType.objects.get(id=pk)
            d.delete()
            return redirect('/conf/documenttypes')
    else:
        return redirect('/app/login')


def custodytypes(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            d = custodytype.objects.filter(company=e.company)
            context = {"Title": "Custody Types", "data": d}
            return render(request, "company/custodytypes.html", context)
    else:
        return redirect('/app/login')


def createcustodytype(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create Custody Types"}
            return render(request, "company/createcustodytypes.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            Number = datetime.datetime.now().timestamp()
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            custodytype.objects.create(company=e.company, arName=arName, enName=enName, number=Number)
            return redirect("/conf/custodytypes")
    else:
        return redirect('/app/login')


def editcustodytype(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            ct = custodytype.objects.get(id=pk)
            context = {"Title": "Create Custody Types", "data": ct}
            return render(request, "company/createcustodytypes.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            ct = custodytype.objects.get(id=pk)
            ct.company = e.company
            ct.arName = arName
            ct.enName = enName
            ct.save()
            return redirect("/conf/custodytypes")
    else:
        return redirect('/app/login')


def delcustodytype(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            ct = custodytype.objects.get(id=pk)
            ct.delete()
            return redirect("/conf/custodytypes")

    else:
        return redirect('/app/login')


def brand(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            d = brands.objects.filter(company=e.company)
            context = {"Title": "brand", "data": d}
            return render(request, "company/brand.html", context)
    else:
        return redirect('/app/login')


def createbrand(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            context = {"Title": "Create brand"}
            return render(request, "company/createbrand.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            Number = datetime.datetime.now().timestamp()
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            brands.objects.create(company=e.company, arName=arName, enName=enName, number=Number)
            return redirect("/conf/brand")
    else:
        return redirect('/app/login')


def editbrand(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            ct = brands.objects.get(id=pk)
            context = {"Title": "Create  brand", "data": ct}
            return render(request, "company/createbrand.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            b = brands.objects.get(id=pk)
            b.company = e.company
            b.arName = arName
            b.enName = enName
            b.save()
            return redirect("/conf/brand")
    else:
        return redirect('/app/login')


def delbrand(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            ct = brands.objects.get(id=pk)
            ct.delete()
            return redirect("/conf/brand")

    else:
        return redirect('/app/login')


def models(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            bm = brandModel.objects.filter(company=e.company)
            context = {"Title": "brand", "data": bm}
            return render(request, "company/models.html", context)
    else:
        return redirect('/app/login')


def createmodel(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            ct = custodytype.objects.filter(company=e.company)
            b = brands.objects.filter(company=e.company)
            context = {"Title": "Create Model", "ct": ct, "b": b}
            return render(request, "company/createmodel.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            custodyt = request.POST["custodytype"]
            ct = custodytype.objects.get(id=custodyt)
            brnd = request.POST["brand"]
            b = brands.objects.get(id=brnd)
            brandModel.objects.create(company=e.company, arName=arName, enName=enName, custodytype=ct, brand=b)
            return redirect("/conf/models")
    else:
        return redirect('/app/login')


def editmodel(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            mod = brandModel.objects.get(id=pk)
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            ct = custodytype.objects.filter(company=e.company)
            b = brands.objects.filter(company=e.company)
            context = {"Title": "Create Model", "data": mod, "ct": ct, "b": b}
            return render(request, "company/createmodel.html", context)
        elif request.method == "POST":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            arName = request.POST["arName"]
            enName = request.POST["enName"]
            custodyt = request.POST["custodytype"]
            ct = custodytype.objects.get(id=custodyt)
            brnd = request.POST["brand"]
            b = brands.objects.get(id=brnd)
            m = brandModel.objects.get(id=pk)
            m.company = e.company
            m.arName = arName
            m.enName = enName
            m.custodytype = ct
            m.brand = b
            m.save()
            return redirect("/conf/models")
    else:
        return redirect('/app/login')


def delmodel(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            bm = brandModel.objects.get(id=pk)
            bm.delete()
            return redirect("/conf/models")

    else:
        return redirect('/app/login')


def usersetting(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            if u.is_superuser == True:
                return redirect('/app/dashboard')
            else:
                e = Employees.objects.get(user=uid)
                q = Employees.objects.filter(company=e.company)
                context = {"Title": "Gareeb | Manage Access", "data": q}
                return render(request, "company/usersetting.html", context)
    else:
        return redirect('/app/login')


def createusersetting(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            e = Employees.objects.get(id=pk)
            context = {"Title": "Create User Setting","data":e}
            return render(request, "company/createusersetting.html", context)
        elif request.method == "POST":
            new_pas = request.POST["npwd"]
            uid = Employees.objects.get(id=pk)
            user = User.objects.get(username=uid)
            user.set_password(new_pas)
            user.save()
            try:
                HR = request.POST['ishr']
                if HR == "on":
                    ishr = True
                else:
                    ishr = False
            except:
                ishr = False
            try:
                MANAGER = request.POST['ismanager']
                if MANAGER == "on":
                    ismanager = True
                else:
                    ismanager = False
            except:
                ismanager = False

            a = Employees.objects.get(id=pk)
            a.isHr = ishr
            a.isManager = ismanager
            a.save()
            return redirect("/conf/usersetting")
    else:
        return redirect('/app/login')


def systemlookup(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "usersetting"}
            return render(request, "company/systemlookup.html", context)
    else:
        return redirect('/app/login')


#
# def createsystemlookup(request):
#     c = chklogin(request)
#     if c:
#         if request.method == "GET":
#             uid = request.session["userid"]
#             context = {"Title": "Create User Setting"}
#             return render(request, "company/createsystemlookup.html", context)
#     else:
#         return redirect('/app/login')


def systemtasks(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "System tasks"}
            return render(request, "company/systemtasks.html", context)
    else:
        return redirect('/app/login')


def createsystemtasks(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Create System Tasks"}
            return render(request, "company/createsystemtasks.html", context)
    else:
        return redirect('/app/login')


def systemtasksdetail(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Syatem tasks detail"}
            return render(request, "company/systemtasksdetail.html", context)
    else:
        return redirect('/app/login')


def systemsettings(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "System Settings"}
            return render(request, "company/systemsettings.html", context)
    else:
        return redirect('/app/login')


def createsystemsettings(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Create System Settings"}
            return render(request, "company/createsystemsettings.html", context)
    else:
        return redirect('/app/login')


def systemcheck(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "System Check"}
            return render(request, "company/systemcheck.html", context)
    else:
        return redirect('/app/login')


def templates(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Templates"}
            return render(request, "company/templates.html", context)
    else:
        return redirect('/app/login')


def edittemplates(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Templates"}
            return render(request, "company/edittemplates.html", context)
    else:
        return redirect('/app/login')

def qoyodintegration(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Qoyod  Integration"}
            return render(request, "company/qoyodintegration.html", context)
    else:
        return redirect('/app/login')


def zkteco(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            context = {"Title": "Zkteco  Integration"}
            return render(request, "company/zkteco.html", context)
    else:
        return redirect('/app/login')
