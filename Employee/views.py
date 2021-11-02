from django.shortcuts import render, redirect
from home.views import chklogin
from home.models import Employees, JobPosition, Department, CreateContracts, JobTitle, EmployementGrades,EmployementLevel,location,costcenter,allowances
from HR.models import Assets, notes
from django.contrib.auth.models import User

from django.http import JsonResponse


# Create your views here.
def employees(request, pk):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            a = Employees.objects.get(id=pk)
            ass = Assets.objects.filter(employee=pk)
            n = notes.objects.filter(employee=pk)
            if (e.company == a.company):
                contract = CreateContracts.objects.filter(Employee=a.id)
                if contract.exists():
                    salarypackage = contract[0].base_salary + contract[0].Housing_Allowance \
                                    # + contract[0].Transport_Allowance + contract[0].otherallowance
                    con = contract[0]
                else:
                    salarypackage = ""
                    con = ""
                context = {"Title": "Employees | HRMS ", "data": a, "data2": con, "salarypackage": salarypackage,
                           "assets": ass, "notes": n}
                return render(request, 'employee/employees.html', context)
            else:
                return redirect('/app/dashboard')
    else:
        return redirect('/app/login')


def createemployees(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            q = Employees.objects.filter(company=e.company, isManager=True)
            d = Department.objects.filter(floor__building__company=e.company)
            j = JobTitle.objects.filter(company=e.company)
            em = EmployementGrades.objects.filter(company=e.company)
            el = EmployementLevel.objects.filter(company=e.company)
            loca = location.objects.filter(company=e.company)
            cc = costcenter.objects.filter(company=e.company)
            allow = allowances.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Create Employees", "data": q, "department": d, "JobTitle": j, "data1": em,"EmployeeLevel":el,
                       "location":loca,"costcenter":cc,"allowance":allow,
                       "emp": "", "contract": ""}
            return render(request, 'employee/createemployees.html', context)

    else:
        return redirect('/app/login')


def ViewEmployees(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            if u.is_superuser == True:
                return redirect('/app/dashboard')
            else:
                e = Employees.objects.get(user=uid)
                q = Employees.objects.filter(company=e.company)
                context = {"Title": "Gareeb | View Employees", "data": q}
                return render(request, 'employee/viewemployees.html', context)
    else:
        return redirect('/app/login')


def EditEmployee(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            q = Employees.objects.filter(company=e.company, isManager=True)
            a = Employees.objects.get(id=pk)
            if (e.company == a.company):
                d = Department.objects.filter(floor__building__company=e.company)
                j = JobTitle.objects.filter(company=e.company)
                em = EmployementGrades.objects.filter(company=e.company)
                el = EmployementLevel.objects.filter(company=e.company)
                loca = location.objects.filter(company=e.company)
                cc = costcenter.objects.filter(company=e.company)
                contract = CreateContracts.objects.filter(Employee=a.id)
                allow = allowances.objects.filter(company=e.company)
                if contract.exists():
                    c = contract[0]
                else:
                    c = ""
                context = {"Title": "Gareeb | Edit Employees", "data": q, "department": d, "JobTitle": j, "data1": em,"EmployeeLevel":el,"location":loca,"costcenter":cc,
                           "emp": a,"allowance":allow, "contract": c}
                return render(request, "employee/createemployees.html", context)
            else:
                return redirect('/app/dashboard')
    else:
        return redirect('/app/login')


def saveemployee(request):
    c = chklogin(request)
    if c:
        empid = request.POST['empid']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['username']
        password = request.POST['password']
        dob = request.POST['dob']
        gender = request.POST['gender']
        nationality = request.POST['nationality']
        idtype = request.POST['idtype']
        idnumber = request.POST['idnumber']
        jtitle = request.POST['jtitle']
        j = JobTitle.objects.get(id=jtitle)
        EmployeeGrade = request.POST['EmployeeGrade']
        gd = EmployementGrades.objects.get(id=EmployeeGrade)
        EmployeeLevel = request.POST['EmployeeLevel']
        el = EmployementLevel.objects.get(id=EmployeeLevel)
        enum = request.POST['enum']
        hdate = request.POST['hdate']
        loca = request.POST['location']
        loc = location.objects.get(id=loca)
        ccenter = request.POST['costcenter']
        cc = costcenter.objects.get(id=ccenter)
        try:
            coach = request.POST['coach']
        except:
            coach = ""
        dept = request.POST['dept']
        d = Department.objects.get(id=dept)
        try:
            manager = request.POST['manager']
        except:
            manager = ""
        try:
            ishr = request.POST['ishr']
            ishr = False
        except:
            ishr = True

        try:
            ismanager = request.POST['ismanager']
            ismanager = False
        except:
            ismanager = True
        if empid == "":
            queryset = User.objects.filter(username=username).values('id')
            if not queryset.exists():
                cuser = User.objects.create_user(username, email, password)
                cuser.first_name = firstname
                cuser.last_name = lastname
                cuser.is_active = True
                cuser.is_staff = True
                try:
                    ishr = request.POST['ishr']
                    ishr = False
                except:
                    ishr = True

                try:
                    ismanager = request.POST['ismanager']
                    ismanager = False
                except:
                    ismanager = True
                cuser.save()
                uid = request.session["userid"]
                u = User.objects.get(id=uid)
                logedinuser = Employees.objects.get(user=u)
                e = Employees.objects.create(user=cuser, Working_Address=loc, Work_Mobile="",
                                             Work_Location="", Work_Email="", Work_Phone=0,
                                             Department=d, Job_position=j,  grade=gd,level=el, Manager=manager, Coach=coach,
                                             Working_hours="8", company=logedinuser.company, isHr=ishr,
                                             isManager=ismanager,
                                             birthdate=dob, gender=gender, nationalid=idnumber, employeenumber=enum,
                                             nationality=nationality, DOJ=hdate, idtype=idtype,ccenter=cc)
                res = {"status": "success", "id": cuser.id}
            else:
                res = {"status": "exists"}
            return JsonResponse(res)
        else:
            u = User.objects.get(id=empid)
            u.first_name = firstname
            u.last_name = lastname
            u.save()
            e = Employees.objects.get(user=empid)
            e.Working_Address = loc
            e.Department = d
            e.Job_position = j
            e.grade = gd
            e.level = el
            e.ccenter = cc
            e.Manager = manager
            e.Coach = coach
            e.isHr = ishr
            e.isManager = ismanager
            e.birthday = dob
            e.gender = gender
            e.nationalid = idnumber
            e.employeenumber = enum
            e.nationality = nationality
            e.DOJ = hdate
            e.idtype = idtype
            e.save()
            res = {"status": "success", "id": u.id}
            return JsonResponse(res)
    else:
        return redirect('/app/login')


def savecontract(request):
    c = chklogin(request)
    if c:
        empid = request.POST['empid']
        cid = request.POST['cid']
        emptype = request.POST['emptype']
        contPerid = request.POST['contPerid']
        sdate = request.POST['sdate']
        endDate = request.POST['endDate']
        notPeriod = request.POST['notPeriod']
        probPeriod = request.POST['probPeriod']
        # bs = request.POST['bs']
        # HA = request.POST['HA']
        # TA = request.POST['TA']
        # OA = request.POST['OA']
        # allowance = request.POST['allowance']
        # allo = allowances.objects.get(id=allowance)


        shiftstart = request.POST['shiftstart']
        shiftend = request.POST['shiftend']
        workhours = request.POST['workhours']
        lunch = request.POST['lunch']
        gosi = request.POST['gosi']
        if gosi == "saudi":
            g = 10
        else:
            g = 12

        if empid == "":

            res = {"status": "error"}
            return JsonResponse(res)
        else:
            u = User.objects.get(id=empid)
            e = Employees.objects.get(user=u)
            d = Department.objects.get(id=e.Department.id)
            if cid == "":
                CreateContracts.objects.create(ContractsReference="Contract For " + u.first_name + " " + u.last_name,
                                               Employee=e, Department=d, Contract_Type=emptype,
                                               Date_From=sdate, Date_To=endDate, Stage=1, GOSI=g, shift_start=shiftstart,
                                               shift_end=shiftend,
                                               workinghours=workhours, breakhours=lunch, employment_type=emptype,
                                               contract_period=contPerid, notice_period=notPeriod,
                                               probation_period=probPeriod,
                                               )
                res = {"status": "success"}
                return JsonResponse(res)

            else:
                contract = CreateContracts.objects.get(id=cid)
                contract.Department = d
                contract.Contract_Type = emptype
                contract.Date_From = sdate
                contract.Date_To = endDate
                contract.Stage = 1
                # contract.base_salary = bs
                # contract.Housing_Allowance = HA
                # contract.Transport_Allowance = TA
                contract.GOSI = g
                contract.shift_start = shiftstart
                contract.shift_end = shiftend
                contract.workinghours = workhours
                contract.breakhours = lunch
                contract.employment_type = emptype
                contract.contract_period = contPerid
                contract.notice_period = notPeriod
                contract.probation_period = probPeriod
                # contract.otherallowance = OA
                # contract.allowance.set(allo)
                contract.save()
                res = {"status": "success"}
                return JsonResponse(res)
    else:
        return redirect('/app/login')


def access(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            if u.is_superuser == True:
                return redirect('/app/dashboard')
            else:
                e = Employees.objects.get(user=uid)
                q = Employees.objects.filter(company=e.company)
                context = {"Title": "Gareeb | Manage Access", "data": q}
                return render(request, 'employee/access.html', context)
    else:
        return redirect('/app/login')


def manageAccess(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            q = Employees.objects.filter(company=e.company, isManager=True)
            a = Employees.objects.get(id=pk)
            context = {"Title": "HRMS | Edit Contract", "data": a}
            return render(request, "employee/ManageAccess.html", context)
        elif request.method == 'POST':
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
            response = redirect('/Employee/access/')
            return response
    else:
        return redirect('/app/login')

def allow(request, pk):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            contract = CreateContracts.objects.get(id=pk)
            allow = allowances.objects.filter(company=e.company)
            context = {"Title": "Gareeb | Create salary", "allowance": allow,
                       "contract": contract}
            return render(request, 'employee/allowance.html', context)
        elif request.method == 'POST':
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            bs = request.POST['bs']
            allo = request.POST['allow']
            allowance = [x.enName for x in allowances.objects.filter(company=e.company)]
            allowance_id = []
            for x in allowance:
                allowance_id.append(int(request.POST.get(x))) if request.POST.get(x) else print("Error")
            contract = CreateContracts.objects.get(id=pk)
            contract.base_salary = bs
            contract.Housing_Allowance = allo
            for x in allowance_id:
                contract.allowance.add(allowances.objects.get(id=x))
            contract.save()
            return redirect("/Employee/salarystr")
    else:
        return redirect('/app/login')


def salarystr(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = User.objects.get(id=uid)
        if u.is_superuser == True:
            return redirect('/app/dashboard')
        else:
            e = Employees.objects.get(user=uid)
            hr = request.session["ishr"]
            if hr:
                con= CreateContracts.objects.filter(Employee__company=e.company)
            else:
                con = CreateContracts.objects.filter(Employee=e)
            context = {"Title": "HRMS | Contracts", "data": con}
            return render(request, 'employee/salarystructure.html', context)
    else:
     return redirect('/app/login')
