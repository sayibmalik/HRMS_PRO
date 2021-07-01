from django.shortcuts import render, redirect
from home.models import Company, Building, Floor,Employees, Department
from Site.models import Userdetails
from django.contrib.auth.models import User
from home.views import chklogin


# Create your views here.
def Users(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        user = User.objects.get(id=uid)
        if user.is_superuser == True:
            u = Userdetails.objects.all()
            context = {"Title": "HRMS | user", "data": u}
            return render(request, "setting/users.html", context)
        else:
            return redirect('/app/dashboard')
    else:
        return redirect('/app/login')


def CreateUser(request):
    return render(request, 'Setting/createuser.html')


def Companies(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        user = User.objects.get(id=uid)
        if user.is_superuser == True:
            c = Company.objects.all()
            context = {"Title": "HRMS | Companies", "data": c}
            return render(request, "setting/companies.html", context)
        else:
            e = Employees.objects.get(user=user)
            return redirect("/Setting/editcompany/" + str(e.company.id))
    else:
        return redirect('/app/login')


def delcompany(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            if user.is_superuser == True:
                pk = request.POST["id"]
                c = Company.objects.get(id=pk)
                c.delete()
                return redirect("/Setting/companies/")
            else:
                return redirect("/app/dashboard")
    else:
        return redirect('/app/login')


def Editcompany(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            a = Company.objects.get(id=pk)
            if user.is_superuser == True:
                context = {"Title": "HRMS | Edit Company", "data": a}
                return render(request, "setting/createcompany.html", context)
            else:
                e=Employees.objects.get(user=uid)
                if e.company.id == a.id:
                    context = {"Title": "HRMS | Edit Company", "data": a}
                    return render(request, "setting/createcompany.html", context)
                else:
                    return redirect("/Setting/editcompany/"+str(e.company.id))
        elif request.method == 'POST':
            Company_Name = request.POST['companyname']
            Address1 = request.POST['street1']
            Address2 = request.POST['street2']
            Pincode = request.POST['pincode']
            State = request.POST['state']
            City = request.POST['city']
            Companytagline = request.POST['companytagline']
            Website = request.POST['website']
            Phone = request.POST['phone']
            Mail = request.POST['email']
            Tin = request.POST['tin']
            Companyreg = request.POST['companyreg']
            Currency = request.POST['currency']
            # Parentcompany = request.POST['parentcompany']
            Reportfooter = request.POST['rfooter']
            Twitter = request.POST['twitter']
            Facebook = request.POST['fb']
            Git = request.POST['github']
            Linkedin = request.POST['linkedin']
            Partner = request.POST['partner']
            c = Company.objects.get(id=pk)
            c.Company_Name = Company_Name
            c.Address1 = Address1
            c.Address2 = Address2
            c.Pin_code = Pincode
            c.State = State
            c.City = City
            c.Company_Tagline = Companytagline
            c.Website = Website
            c.Email = Mail
            c.Phone = Phone
            c.Tin = Tin
            c.Company_registry = Companyreg
            c.Currency = Currency
            c.Reportfooter = Reportfooter
            c.Twitter = Twitter
            c.Facebook = Facebook
            c.Git = Git
            c.Linkedin = Linkedin
            c.Partner = Partner
            c.save()
            response = redirect('/Setting/companies')
            return response
    else:
        return redirect('/app/login')


def CreateCompany(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            context = {"Title": "Gareeb | Create Company"}
            return render(request, "setting/createcompany.html", context)
        elif request.method == 'POST':
            Company_Name = request.POST['companyname']
            Address1 = request.POST['street1']
            Address2 = request.POST['street2']
            Pincode = request.POST['pincode']
            State = request.POST['state']
            City = request.POST['city']
            Companytagline = request.POST['companytagline']
            Website = request.POST['website']
            Phone = request.POST['phone']
            Mail = request.POST['email']
            Tin = request.POST['tin']
            Companyreg = request.POST['companyreg']
            Currency = request.POST['currency']
            # Parentcompany = request.POST['parentcompany']
            Reportfooter = request.POST['rfooter']
            Twitter = request.POST['twitter']
            Facebook = request.POST['fb']
            Git = request.POST['github']
            Linkedin = request.POST['linkedin']
            Partner = request.POST['partner']
            Company.objects.create(Company_Name=Company_Name, Address1=Address1, Address2=Address2, Pin_code=Pincode,
                                   State=State, City=City,
                                   Company_Tagline=Companytagline, Website=Website, Phone=Phone, Email=Mail, Tin=Tin,
                                   Company_registry=Companyreg,
                                   Currency=Currency, Reportfooter=Reportfooter,
                                   Twitter=Twitter, Facebook=Facebook, Git=Git, Linkedin=Linkedin, Partner=Partner)
            response = redirect('/Setting/companies')
            return response
    else:
        return redirect('/app/login')

def Buildings(request):
    c = chklogin(request)
    if c:
        p = Building.objects.all()
        context = {"Title": "Gareeb | Setting", "data": p}
        return render(request, 'setting/buildings.html', context)
    else:
        return redirect('/app/login')


def CreateBuilding(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            return render(request, 'setting/createbuilding.html')

        elif request.method == "POST":
            code = request.POST["code"]
            name = request.POST["name"]
            address = request.POST["address"]
            Building.objects.create( code=code, buildingName=name, Address=address)
            response = redirect('/Setting/buildings')
            return response
    else:
        return redirect('/app/login')



def Editbuilding(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            p = Building.objects.get(id=pk)
            context = {"Title": "HRMS | Edit building", "data": p}
            return render(request, "setting/createbuilding.html",context)
        elif request.method == 'POST':
            code = request.POST["code"]
            name = request.POST["name"]
            address = request.POST["address"]
            p = Building.objects.get(id=pk)
            p.buildingName = name
            p.code = code
            p.Address = address
            p.save()
            response = redirect('/Setting/buildings')
            return response
    else:
        return redirect('/app/login')

def delbuilding(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["building_id"]
            p = Building.objects.get(id=pk)
            p.delete()
            return redirect("/Setting/buildings/")
    else:
        return redirect('/app/login')



def Floors(request):
    c = chklogin(request)
    if c:
        p = Floor.objects.all()
        context = {"Title": "Gareeb | Setting", "data": p}
        return render(request, 'setting/floors.html', context)
    else:
        return redirect('/app/login')



def CreateFloor(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            c= Building.objects.all()
            context = {"Title": "Gareeb | Create Floor", "data": c }
            return render(request, "setting/createfloor.html", context)
        elif request.method == 'POST':
            title = request.POST['title']
            user = Building.objects.get(id=pk)
            Floor.objects.create(title=title, building=user)
        return render(request, 'setting/createfloor.html')
    else:
        return redirect('/app/login')



def Editfloor(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            # p = Floor.objects.get(id=)
            context = {"Title": "HRMS | Edit Floor", "data": p}
            return render(request, "setting/createfloor.html",context)
        elif request.method == 'POST':
            title = request.POST["title"]
            p = Floor.objects.get(id=pk)
            p.title = title
            p.save()
            response = redirect('/Setting/floors')
            return response
    else:
        return redirect('/app/login')

def delfloor(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["floor_id"]
            p = Floor.objects.get(id=pk)
            p.delete()
            return redirect("/Setting/floors/")
    else:
        return redirect('/app/login')


def departments(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = Employees.objects.get(user=uid)
        p = Department.objects.filter(floor__building__company=u.company)
        context = {"Title": "Gareeb | Setting", "data": p}
        return render(request, 'setting/departments.html', context)
    else:
        return redirect('/app/login')


def CreateDepartments(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid=request.session["userid"]
            u=Employees.objects.get(user=uid)
            c = Floor.objects.filter(building__company=u.company)
            context = {"Title": "Gareeb | Setting", "data": c}
            return render(request, 'setting/createdepartments.html',context)

        elif request.method == "POST":
            title = request.POST["title"]
            floor = request.POST["floor"]
            f = Floor.objects.get(id=floor)
            Department.objects.create( title=title, floor=f)
            response = redirect('/Setting/departments')
            return response
    else:
        return redirect('/app/login')

def Editdepartment(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            u = Employees.objects.get(user=uid)
            c = Floor.objects.filter(building__company=u.company)
            p = Department.objects.get(id=pk)
            context = {"Title": "HRMS | Edit Department", "data2": p, "data": c}
            return render(request, "setting/createdepartments.html",context)
        elif request.method == 'POST':
            title = request.POST["title"]
            floor = request.POST["floor"]
            f = Floor.objects.get(id=floor)
            p = Department.objects.get(id=pk)
            p.title = title
            p.floor = f
            p.save()
            response = redirect('/Setting/departments')
            return response
    else:
        return redirect('/app/login')

def deldepartment(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["department_id"]
            p = Department.objects.get(id=pk)
            p.delete()
            return redirect("/Setting/departments/")
    else:
        return redirect('/app/login')

def viewcompany(request):
    return render(request, 'setting/viewcompany.html')

def UserEmployees(request,pk):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid=request.session["userid"]
            u=User.objects.get(id=uid)
            if not u.is_superuser == True:
                return redirect('/app/dashboard')
            else:
                e=Employees.objects.get(user=pk)
                q = Employees.objects.filter(company=e.company)
                context = {"Title": "Gareeb | View Employees", "data": q}
                return render(request, 'setting/useremployees.html', context)
    else:
        return redirect('/app/login')

