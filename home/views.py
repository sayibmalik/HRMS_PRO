from django.shortcuts import render, redirect
from django.db.models import Sum
from django.core.files.storage import FileSystemStorage
from .models import Announcements,LeavesRequest, Company,Employees,Department,JobPosition,Building,Floor\
    ,Project,JobTitle,location,EmployementGrades,EmployementLevel
from Site.models import Product,Userdetails,Billingaddress,Bills
from django.contrib.auth.models import User , Permission
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage
from Recruitment.models import Jobs
from Attendance .models import Timesheet
from django.contrib import messages
from Site.models import UserMembership,Subscription


# Create your views here.

def index(request):
    c= chklogin(request)
    if c:
        try:
            uid = request.session["userid"]
            u = User.objects.get(id=uid)
            user_membership = UserMembership.objects.get(user=uid)
            subscriptions = Subscription.objects.filter(user_membership=user_membership).exists()
            if subscriptions == False:
                return redirect('/Site/upgradeplan')
        except UserMembership.DoesNotExist:
            return redirect('/upgradeplan')
        if u.is_superuser == True:
            emp=0
            tu = User.objects.all()
            com = Company.objects.all()
            bill = Bills.objects.filter(paidStatus=True).aggregate(Sum('Amount'))
            context = {"user": u, "tu": tu.count, "com": com.count, "bill": bill["Amount__sum"]}
            return render(request, 'index.html', context)
        else:
            try:
                e=Employees.objects.get(user=uid)
            except:
                return redirect('/app/signup/')
            emp=e
            users = Employees.objects.get(user=uid)
            q = Employees.objects.filter(company=users.company)
            ann = Announcements.objects.filter(company=e.company)
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            r = Jobs.objects.filter(company=e.company)
            p = Project.objects.filter(company=e.company, active=True)
            t = Timesheet.objects.filter(user=uid)
            hr = request.session['ishr']
            if hr:
                b = LeavesRequest.objects.filter(user__company=users.company)
            else:
                b = LeavesRequest.objects.filter(user=e)
            context = {"user": u, "emp": emp,"ann":ann,"users":q.count,"jobs":r,"projects":p.count,"data":t,"leaves":b.count}
            return render(request, 'index.html',context)
    else:
        return redirect('/app/login')

def Blocks(request):
    return render(request, 'blocks.html')

def Carousels(request):
    return render(request, 'carousels.html')

def Forms(request):
    return render(request, 'forms.html')

def Pricing(request):
    return render(request, 'pricing.html')

def calendar(request):
    return render(request, 'calendar.html')

def CreateMeeting(request):
    return render(request, 'createmeeting.html')

def Meetings(request):
    return render(request, 'meetings.html')

def Industry(request):
    return render(request, 'industry.html')

def CreateIndustry(request):
    return render(request, 'createindustry.html')

def Countries(request):
    return render(request, 'countries.html')

def FedStates(request):
    return render(request, 'fedstates.html')

def CountryGroup(request):
    return render(request, 'countrygroup.html')

def Banks(request):
    return render(request, 'banks.html')

def CreateBank(request):
    return render(request, 'createbank.html')

def BankAccounts(request):
    return render(request, 'bankaccounts.html')

def CreateBankAccounts(request):
    return render(request, 'createbankaccounts.html')

def Dashboard(request):

    return render(request, 'home/dashboard.html')

def DiscussInbox(request):
    return render(request, 'discussinbox.html')

def DiscussGeneral(request):
    return render(request, 'discussgeneral.html')

def GeneralPublicChannels(request):
    return render(request, 'generalpublicchannels.html')

def CreatePublicChannels(request):
    return render(request, 'createpublicchannels.html')

def Badges(request):
    return render(request, 'badges.html')

def createBadges(request):
    return render(request, 'createbadges.html')

def CreateChallenges(request):
    return render(request, 'createchallenges.html')

def RegularizationCategory(request):
    return render(request, 'regularizationcategory.html')

def CreateRegularizationCategory(request):
    return render(request, 'createregularizationcategory.html')

def Expenses(request):
    return render(request, 'expenses.html')

def CreateExpenses(request):
    return render(request, 'createexpenses.html')

def MyReports(request):
    return render(request, 'myreports.html')

def CreateReport(request):
    return render(request, 'createreport.html')

def ExpensesReportsToPay(request):
    return render(request, 'expensesreportstopay.html')

def CreateExpensesReportsToPay(request):
    return render(request, 'createexpensesreportstopay.html')

def AllExpenses(request):
    return render(request, 'allexpenses.html')

def ExpensesReport(request):
    return render(request, 'expensesreport.html')

def ExpensesProducts(request):
    return render(request, 'expensesproducts.html')

def CreateExpensesProducts(request):
    return render(request, 'createexpensesproducts.html')

def ViewExpensesProducts(request):
    return render(request, 'viewexpensesproducts.html')

def Login(request):
    if request.method=="GET":
        c = chklogin(request)
        if c:
            return redirect('/app/dashboard')
        else:
            return render(request, 'home/login.html')
    elif request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(request, username=u, password=p)
        if user:
            request.session['userid'] = user.id
            request.session['username'] = u
            request.session['password'] = p
            request.session['name'] = user.first_name+ " " +user.last_name
            if user.is_superuser:
                request.session['superuser'] = True
            else:
                request.session['superuser'] = False
            try:
                e=Employees.objects.get(user=user)
                hr=e.isHr
                manager=e.isManager
            except:
                hr=False
                manager=False
            request.session['ishr'] = hr
            request.session['ismanager'] = manager
            response = redirect('/app/dashboard')
            return response
        else:
            response = redirect('/app/login/?msg=Invalid credentials')
            return response

def Signup(request):
    if request.method == 'GET':
        c = chklogin(request)
        stage=1
        if c:
            try:
                stage = request.session['stage']
                if stage == 1:
                    stage = 2
                elif stage == 5:
                    response = redirect('/app/dashboard')
                    return response
                else:
                    stage = request.session['stage']
            except:
                uid = request.session["userid"]
                try:
                    u = Userdetails.objects.get(user=uid)
                    c = Company.objects.get(user=uid)
                    try:
                        b = Billingaddress.objects.get(user=uid)
                        # stage = 5
                        return redirect("")
                    except:
                        stage = 4
                except:
                    stage=2
        else:
            stage = 1
        p=Product.objects.all()
        request.session['stage']=stage
        stg=request.session['stage']
        context = {"stage": stg ,"plan":p,}
        return render(request, 'home/signup.html', context)
    elif request.method == 'POST':
        stage = request.session['stage']
        if stage==1:
            fname = request.POST['fname']
            lname = request.POST['lname']
            username = request.POST['email']
            num = request.POST['Number']
            email = request.POST['email']
            password = request.POST['password']
            queryset = User.objects.filter(username=username).values('id')
            if not queryset.exists():
                cuser = User.objects.create_user(username, email, password)
                cuser.first_name = fname
                cuser.last_name = lname
                cuser.is_active = True
                cuser.is_staff = True
                cuser.save()
                Userdetails.objects.create(user=cuser,number=num,Balance=0)
                request.session['userid'] = cuser.id
                request.session['username'] = username
                request.session['password'] = password
                request.session['name'] = cuser.first_name + " " + cuser.last_name
                request.session['superuser'] = False
                hr = True
                manager = True
                request.session['ishr'] = hr
                request.session['ismanager'] = manager
                request.session['stage'] = 2
            else:
                messages.warning(request, 'Email is already exist')
        elif stage == 2:
            p = request.POST["pricing"]
            plan = Product.objects.get(id=p)
            uid = request.session['userid']
            user = User.objects.get(id=uid)
            u = Userdetails.objects.get(user=user)
            u.plan = plan
            u.save()
            request.session['stage'] = 3
        elif stage == 3:
            uid = request.session['userid']
            user = User.objects.get(id=uid)
            company = request.POST['companyname']
            companytagline = request.POST['companytagline']
            address1 = request.POST['address1']
            address2= request.POST['address2']
            state= request.POST['state']
            city= request.POST['city']
            pincode= request.POST['pincode']
            ud=Userdetails.objects.get(user=user)
            nc=Company.objects.create(user=user,Company_Name=company, Company_Tagline=companytagline, Address1=address1,Address2=address2
                                   ,State=state,City=city,Pin_code=pincode)
            b=Building.objects.create(buildingName="Your Building",code="001",Address=address1,company=nc)
            f=Floor.objects.create(title="Floor 1" , building=b)
            d=Department.objects.create(title="Administration",floor=f)
            j=JobTitle.objects.create(jobtitleEn="Administration",jobtitleAr="الادارة",company=nc)
            lo=location.objects.create(locationnameAR=address1,locationnameEN=address2,cityAR=city,cityEN=city,stateAR=state,stateEN=state,
                                    postalCode=pincode,telephone=ud.number,company=nc)
            grd = EmployementGrades.objects.create(titleEn="First Grade",titleAr="الصف الاول",company=nc)
            lev = EmployementLevel.objects.create(titleEn="Level One",titleAr=" المستوى الأول",company=nc)
            Employees.objects.create(user=user, Working_Address=lo, Work_Mobile=ud.number,
                                     Work_Location=address2, Work_Email=user, Work_Phone=ud.number,
                                     Department=d, Job_position=j, Manager=user, Coach="",
                                     Working_hours="8", company=nc,isHr=True,isManager=True,
                                     birthdate="2001-01-01", gender="Male", nationalid="", employeenumber="",
                                     nationality="", DOJ="2001-01-01", idtype="Iqamah",grade=grd,level=lev
                                     )
            request.session['stage'] = 4
        elif stage == 4:
            uid = request.session['userid']
            user = User.objects.get(id=uid)
            billingaddress = request.POST['billingaddress']
            zipcode = request.POST['zipcode']
            city = request.POST['city']
            state = request.POST['state']
            country = request.POST['country']
            Billingaddress.objects.create(user=user,address=billingaddress,zip_code=zipcode,City=city,State=state,Country=country)
            request.session['stage'] = 5

        response = redirect('/app/signup')
        return response



def logout(request):
    c= chklogin(request)
    if c:
        del request.session['userid']
        del request.session['username']
        del request.session['password']
        del request.session['superuser']
        del request.session['name']
        del request.session['ishr']
        del request.session['ismanager']
        request.session.modified = True
        response = redirect('/')
        return response
    else:
        return redirect('/app/login')


def chklogin(request):
    log = False
    try:
        u = request.session['username']
        p = request.session['password']
        user = authenticate(request, username=u, password=p)
        if user:
            log = True
    except:
        log = False
    return log

def Changelang(request):
    try:
        if request.session["lang"]== "AR":
            request.session["lang"]="EN"
        else:
            request.session["lang"] = "AR"
    except:
        request.session["lang"] = "EN"
    return redirect("/app/dashboard")

def FreeSignUp(request):
    context = {"Title":"Free Sign Up | Gareeb"}
    return render(request , "home/freeSignup.html", context)

def forgetpasscode(request):
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()
        return redirect("/app/login")
    return render(request,"home/forgetpasscode.html")


import random

def reset_password(request):
    un = request.GET["username"]
    try:
        user = get_object_or_404(User,username=un)
        otp = random.randint(1000,9999)
        msz = "Dear {} \nWe received a request to reset your Gareeb HRM account password.\nEnter the following password reset code {}\n \nThanks&Regards \nGareeb".format(user.first_name, otp)
        try:
            email = EmailMessage("{} is your Gareeb HRM account recovery code".format(otp),msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            return JsonResponse({"status":"error","email":user.email})
    except:
        return JsonResponse({"status":"failed"})







