from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from home.models import Announcements,Company, Contact, CreateContracts,JobPosition,Employees,Department,documentType
from .models import Documents, Assets, notes
from django.contrib.auth.models import User
from home.views import chklogin
# Create your views here.
def Appraisals(request):
    return render(request, 'HR/appraisals.html')

def announcements(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = User.objects.get(id=uid)
        if u.is_superuser == True:
            return redirect('/app/dashboard')
        else:
            e = Employees.objects.get(user=uid)
            q = Announcements.objects.filter(company=e.company)
            context = {"Title": "HRMS | Announcements", "data": q}
            return render(request, "HR/announcements.html", context)
    else:
        return redirect('/app/login')

def createAnnouncements(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            q = Announcements.objects.all()
            context = {"Title": "Gareeb | Create Announcements", "data": q}
            return render(request, 'HR/createannouncements.html', context)
        elif request.method == 'POST':
            try:
                is_general = request.POST['inGeneral']
                g = True
            except:
                g = False
            title = request.POST['title']
            codeno = request.POST['code']
            date = request.POST['datereq']
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            letter =request.POST["letter"]
            Announcements.objects.create(is_general_announcements=g, title=title, code_no=codeno,
                                         requestedDate=date, company=e.company,letter=letter)
            response = redirect('/HR/announcements')
            return response
    else:
        return redirect('/app/login')

def Editannouncements(request, pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a = Announcements.objects.get(id=pk)
            co = Company.objects.all()
            context = {"Title": "HRMS | Edit Announcements", "data": a ,"data1":co}
            return render(request, "HR/createannouncements.html", context)
        elif request.method == "POST":
            try:
                is_general = request.POST['inGeneral']
                g = True
            except:
                g = False
            ti = request.POST['title']
            cod = request.POST['code']
            dat = request.POST['datereq']
            let =request.POST["letter"]
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            ea = Announcements.objects.get(id=pk)
            ea.is_general_announcements = g
            ea.title = ti
            ea.code_no = cod
            ea.requestedDate = dat
            ea.letter = let
            ea.company = e.company
            ea.save()
            response = redirect('/HR/announcements')
            return response
    else:
        return redirect('/app/login')

def delannouncement(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c =Announcements .objects.get(id=pk)
            c.delete()
            return redirect("/HR/announcements/")
    else:
        return redirect('/app/login')

def createAppraisals(request):
    return render(request, 'HR/createappraisals.html')

def approveAnnouncements(request):
    return render(request, 'HR/approveannouncements.html')

def answerAppraisal(request):
    return render(request, 'HR/answerappraisal.html')

def ViewAppraisal(request):
    return render(request, 'HR/viewappraisal.html')

def EmployeeTransfer(request):
    return render(request, 'HR/employeetransfer.html')

def EmployeesSettings(request):
    return render(request, 'HR/employeessettings.html')

def Contracts(request):
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
            return render(request, 'HR/contracts.html', context)
    else:
        return redirect('/app/login')

def createContracts(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            le = Employees.objects.filter(company=e.company)
            d = Department.objects.filter(floor__building__company=e.company)
            j = JobPosition.objects.filter(company=e.company)
            context = {"data": le,"department": d, "jobposition": j}
            return render(request, 'HR/createcontracts.html',context)
        elif request.method == "POST":
            ContractsReference= request.POST["ref"]
            Employee= request.POST["Employee"]
            e= Employees.objects.get(id=Employee)
            Job_Position= request.POST["Job_Position"]
            j= JobPosition.objects.get(id=Job_Position)
            department= request.POST["Department"]
            d= Department.objects.get(id=department)
            ctype= request.POST["ctype"]
            Date_From= request.POST["Date_From"]
            Date_To= request.POST["Date_To"]
            Stage= request.POST["stage"]
            Wage= request.POST["wage"]
            HA= request.POST["HA"]
            TA= request.POST["TA"]
            GOSI= request.POST["GOSI"]
            Shiftstart= request.POST["shiftstart"]
            Shiftend= request.POST["shiftend"]
            hours= request.POST["hours"]
            brk= request.POST["break"]

            CreateContracts.objects.create(ContractsReference=ContractsReference,Employee=e,Job_Position=j,
                                           Department=d,Contract_Type=ctype,base_salary=Wage,Housing_Allowance=HA,Transport_Allowance=TA,GOSI=GOSI,
                                           Date_From=Date_From,Date_To=Date_To,shift_start=Shiftstart,shift_end=Shiftend,workinghours=hours,breakhours=brk,Stage=Stage)
            return redirect("/HR/contracts/")
    else:
        return redirect('/app/login')

def editContract(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a = CreateContracts.objects.get(id=pk)
            context = {"Title": "HRMS | Edit Contract", "data": a}
            return render(request, "HR/editcontract.html", context)
        elif request.method == 'POST':
            Date_From = request.POST["Date_From"]
            Date_To = request.POST["Date_To"]
            a = CreateContracts.objects.get(id=pk)
            a.Date_From = Date_From
            a.Date_To = Date_To
            a.save()
            response = redirect('/HR/contracts')
            return response
    else:
        return redirect('/app/login')

def Recruitment(request):
    return render(request, 'HR/recruitment.html')

def Contactss(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        u = User.objects.get(id=uid)
        if u.is_superuser == True:
            return redirect('/app/dashboard')
        else:
            e = Employees.objects.get(user=uid)
            c= Contact.objects.filter(companyContact=e.company)
            context = {"Title": "Gareeb | Contacts", "data": c}
            return render(request, 'HR/contacts.html', context)
    else:
        return redirect('/app/login')

def CreateContacts(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            context = {"Title": "Gareeb | Create Contact"}
            return render(request, 'HR/createcontacts.html', context)
        elif request.method == 'POST':
            Employee = request.POST['employeename']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            pincode = request.POST['pincode']
            country = request.POST['country']
            tin = request.POST['tin']
            jobPosition = request.POST['jobposition']
            phone  = request.POST['phone']
            mobile = request.POST['mobile']
            email= request.POST['email']
            website  = request.POST['website']
            title  = request.POST['title']
            language = request.POST['language']
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            Contact.objects.create(name=Employee,address1=address1,address2=address2, pincode=pincode, country=country, tin=tin,jobPosition=jobPosition,
                                         phone=phone, mobile=mobile, email=email, website=website, title=title,language=language,companyContact=e.company)
            response = redirect('/HR/contacts')
            return response
    else:
        return redirect('/app/login')

def delcontact(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            dc = Contact.objects.get(id=pk)
            dc.delete()
            return redirect("/HR/contacts")
    else:
        return redirect('/app/login')


def ViewContact(request ,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a = Contact.objects.get(id=pk)
            context = {"Title": "HRMS | Edit Contact", "data": a}
            return render(request, "HR/createcontacts.html", context)
        elif request.method == 'POST':
            Employee = request.POST['employeename']
            address1 = request.POST['address1']
            address2 = request.POST['address2']
            pincode = request.POST['pincode']
            country = request.POST['country']
            tin = request.POST['tin']
            jobPosition = request.POST['jobposition']
            phone = request.POST['phone']
            mobile = request.POST['mobile']
            email = request.POST['email']
            website = request.POST['website']
            title = request.POST['title']
            language = request.POST['language']
            a = Contact.objects.get(id=pk)
            a.name = Employee
            a.address1 = address1
            a.address2 = address2
            a.pincode = pincode
            a.country = country
            a.tin = tin
            a.jobPosition = jobPosition
            a.phone = phone
            a.mobile = mobile
            a.email = email
            a.website = website
            a.title = title
            a.language = language
            a.save()
            response = redirect('/HR/contacts')
            return response
    else:
        return redirect('/app/login')

def ContactTag(request):
    return render(request, 'HR/contacttags.html')

def CreateContactTags(request):
    return render(request, 'HR/createcontacttags.html')

def ContactTitles(request):
    return render(request, 'HR/contacttitles.html')

def ContractTemplate(request,pk):
    c = chklogin(request)
    if c:
        e=Employees.objects.get(id=pk)
        c=CreateContracts.objects.filter(Employee=pk)
        context={"emp":e,"contract":c[0]}
        return render(request, 'HR/contracttemplate.html',context)
    else:
        return redirect('/app/login')

def document(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        c = Documents.objects.filter(employee__company=e.company)
        context = {"data":c}
        return render(request, 'HR/documents.html', context)
    else:
        return redirect('/app/login')

def Createdocuments(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            le = Employees.objects.filter(company=e.company)
            dt = documentType.objects.filter(company=e.company)
            context = {"data": le,"doctype":dt}
            return render(request, 'HR/createdocuments.html', context)
        elif request.method == 'POST':
            Title = request.POST['title']
            Employee = request.POST['empname']
            e = Employees.objects.get(id=Employee)
            fs = FileSystemStorage()
            Document = request.FILES['doc']
            name = fs.save(Document.name, Document)
            Type = request.POST['doctype']
            dt = documentType.objects.get(id=Type)
            Documents.objects.create(title=Title,employee=e,file=name,doctype=dt)

            response = redirect('/HR/documents')
            return response
    else:
        return redirect('/app/login')


def Editdocuments(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            d = Documents.objects.get(id=pk)
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            le = Employees.objects.filter(company=e.company)
            dt = documentType.objects.filter(company=e.company)
            context = {"data2": d ,"data": le, "doctype":dt}
            return render(request, 'HR/createdocuments.html', context)
        elif request.method == 'POST':
            Title = request.POST['title']
            Employee = request.POST['empname']
            e = Employees.objects.get(id=Employee)
            fs = FileSystemStorage()
            Document = request.FILES['doc']
            name = fs.save(Document.name, Document)
            Type = request.POST['doctype']
            dt = documentType.objects.get(id=Type)
            a = Documents.objects.get(id=pk)
            a.title = Title
            a.employee = e
            a.doctype = dt
            a.file = name
            a.save()
            response = redirect('/HR/documents')
            return response
    else:
        return redirect('/app/login')

def deldocument(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["docid"]
            c = Documents.objects.get(id=pk)
            c.delete()
            return redirect("/HR/documents/")
    else:
        return redirect('/app/login')

def Notes(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        n = notes.objects.filter(employee__company=e.company)
        context = {"data": n}
        return render(request, 'HR/notes.html',context)
    else:
        return redirect('/app/login')

def Createnotes(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            em = Employees.objects.filter(company=e.company)
            context = {"data": em}
            return render(request, 'HR/createnotes.html',context)
        elif request.method == 'POST':
            Employee = request.POST['emp']
            e = Employees.objects.get(id=Employee)
            Date = request.POST['date']
            Note = request.POST['note']
            uid = request.session["userid"]
            v = Employees.objects.get(user=uid)
            notes.objects.create(employee=e,date=Date,note=Note,addedby=v.user)
            response = redirect('/HR/notes')
            return response
    else:
        return redirect('/app/login')

def Editnotes(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a = notes.objects.get(id=pk)
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            le = Employees.objects.filter(company=e.company)
            context = {"Title": "HRMS | Edit Note", "data2": a , "data":le}
            return render(request, 'HR/createnotes.html',context)
        elif request.method == 'POST':
            Employee = request.POST['emp']
            e = Employees.objects.get(id=Employee)
            Date = request.POST['date']
            Note = request.POST['note']
            uid = request.session["userid"]
            v = Employees.objects.get(user=uid)
            a = notes.objects.get(id=pk)
            a.employee = e
            a.date = Date
            a.addedby = v.user
            a.note = Note
            a.save()
            response = redirect('/HR/notes')
            return response
    else:
        return redirect('/app/login')

def delnotes(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["notesid"]
            c = notes.objects.get(id=pk)
            c.delete()
            return redirect("/HR/notes/")
    else:
        return redirect('/app/login')

def assets(request):
    c = chklogin(request)
    if c:
        uid = request.session["userid"]
        e = Employees.objects.get(user=uid)
        a = Assets.objects.filter(employee__company=e.company)
        context = {"data": a}
        return render(request, 'HR/assets.html',context)
    else:
        return redirect('/app/login')

def Createassets(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            a = Employees.objects.filter(company=e.company)
            context = {"data": a}
            return render(request, 'HR/createassets.html', context)
        elif request.method == 'POST':
            Employee = request.POST['emp']
            em = Employees.objects.get(id=Employee)
            type = request.POST['type']
            number = request.POST['no']
            handover = request.POST['handover']
            status = request.POST['status']
            returndate = request.POST['returndate']
            desc = request.POST['desc']
            Assets.objects.create(employee=em, type=type, number=number, handover=handover,status=status, returndate=returndate,description=desc )
            response = redirect('/HR/assets')
            return response
    else:
        return redirect('/app/login')

def Editassets(request,pk):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            a = Assets.objects.get(id=pk)
            uid = request.session["userid"]
            e = Employees.objects.get(user=uid)
            e = Employees.objects.filter(company=e.company)
            context = {"Title": "HRMS | Edit Asset", "data2": a, "data": e}
            return render(request, 'HR/createassets.html', context)
        elif request.method == 'POST':
            Employee = request.POST['emp']
            e = Employees.objects.get(id=Employee)
            type = request.POST['type']
            number = request.POST['no']
            handover = request.POST['handover']
            status = request.POST['status']
            returndate = request.POST['returndate']
            desc = request.POST['desc']
            a = Assets.objects.get(id=pk)
            a.employee = e
            a.type = type
            a.number = number
            a.handover = handover
            a.status = status
            a.returndate = returndate
            a.description = desc
            a.save()
            response = redirect('/HR/assets')
            return response
    else:
        return redirect('/app/login')

def delassets(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["assetsid"]
            c = Assets.objects.get(id=pk)
            c.delete()
            return redirect("/HR/assets/")
    else:
        return redirect('/app/login')