from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField


# Create your models here.

class Company(models.Model):
    Company_Name = models.CharField(max_length=250)
    Company_Tagline = models.CharField(max_length=250)
    Address1 = models.CharField(max_length=250)
    Address2 = models.CharField(max_length=250)
    Pin_code = models.IntegerField()
    State = models.CharField(max_length=250)
    City = models.CharField(max_length=250)
    # Companytagline = models.CharField(max_length=5000)
    Website = models.URLField(null=True)
    Email = models.EmailField(null=True)
    Tin = models.CharField(max_length=150, null=True)
    Company_registry = models.CharField(max_length=250, null=True)
    Currency = models.CharField(max_length=250, null=True)
    Reportfooter = models.CharField(max_length=250, null=True)
    Twitter = models.CharField(max_length=150, null=True)
    Facebook = models.CharField(max_length=150, null=True)
    Git = models.CharField(max_length=150, null=True)
    Linkedin = models.CharField(max_length=150, null=True)
    # Country=models.CharField(max_length=250)
    Phone = models.CharField(max_length=150, null=True)
    # Fax=models.IntegerField()
    # Tax_id=models.CharField(max_length=250)
    # checkbox = models.BooleanField(default=False)
    Partner = models.CharField(max_length=250, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.Company_Name)


class JobTitle(models.Model):
    jobtitleEn = models.CharField(max_length=200, blank=True, null=True)
    jobtitleAr = models.CharField(max_length=200, blank=True, null=True)
    desEn = models.CharField(max_length=5000, blank=True, null=True)
    desAr = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.jobtitleEn)


class EmployementGrades(models.Model):
    titleEn = models.CharField(max_length=200, blank=True, null=True)
    titleAr = models.CharField(max_length=200, blank=True, null=True)
    desEn = models.CharField(max_length=5000, blank=True, null=True)
    desAr = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.titleEn)


class EmployementLevel(models.Model):
    titleEn = models.CharField(max_length=200, blank=True, null=True)
    titleAr = models.CharField(max_length=200, blank=True, null=True)
    desEn = models.CharField(max_length=5000, blank=True, null=True)
    desAr = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.titleEn)


operationType_CHOICES = [
    ("Salary Addition", "Salary Addition"),
    ("Salary Deduction", "Salary Deduction"),
]

valueType_CHOICES = [
    ("Fixed Amount", "Fixed Amount"),
    ("Percentage from basic salary", "Percentage from basic salary"),
    ("Percentage from basic + salary component", "Percentage from basic + salary component"),
]


class allowances(models.Model):
    operationType = models.CharField(max_length=200, choices=operationType_CHOICES)
    arName = models.CharField(max_length=200, blank=True, null=True)
    enName = models.CharField(max_length=200, blank=True, null=True)
    valueType = models.CharField(max_length=200, choices=valueType_CHOICES)
    value = models.FloatField()
    maxValue = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.enName)


Type_CHOICES = [
    ("Addition", "Addition"),
    ("Deduction", "Deduction"),
]


class deductionAddition(models.Model):
    arName = models.CharField(max_length=200, blank=True, null=True)
    enName = models.CharField(max_length=200, blank=True, null=True)
    opeartionType = models.CharField(max_length=200, choices=Type_CHOICES)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.enName)


class bank(models.Model):
    arName = models.CharField(max_length=200, blank=True, null=True)
    enName = models.CharField(max_length=200, blank=True, null=True)
    transferFees = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.enName)


class insurance(models.Model):
    titleEn = models.CharField(max_length=200, blank=True, null=True)
    titleAr = models.CharField(max_length=200, blank=True, null=True)
    desEn = models.CharField(max_length=5000, blank=True, null=True)
    desAr = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.titleEn)

class holidays(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    nameAR = models.CharField(max_length=250,blank=True,null=True)
    nameEN = models.CharField(max_length=250,blank=True,null=True)
    fromDate = models.DateField()
    toDate = models.DateField()
    def __str__(self):
        return "{}".format(self.nameEN)

class costcenter(models.Model):
    nameAR = models.CharField(max_length=250, blank=True, null=True)
    nameEN = models.CharField(max_length=250, blank=True, null=True)
    desAR = models.CharField(max_length=5000, blank=True, null=True)
    desEN = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return  "{}".format(self.nameEN)

class location(models.Model):
    locationnameAR = models.CharField(max_length=300,blank=True,null=True)
    locationnameEN = models.CharField(max_length=300,blank=True,null=True)
    country = CountryField(blank=True,null=True)
    cityAR = models.CharField(max_length=300,blank=True,null=True)
    cityEN = models.CharField(max_length=300,blank=True,null=True)
    streetAR = models.CharField(max_length=300,blank=True,null=True)
    streetEN = models.CharField(max_length=300,blank=True,null=True)
    stateAR = models.CharField(max_length=300,blank=True,null=True)
    stateEN = models.CharField(max_length=300,blank=True,null=True)
    telephone = models.BigIntegerField(blank=True,null=True)
    postalCode = models.CharField(max_length=300,blank=True,null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.locationnameEN)

class documentType(models.Model):
    titleEn = models.CharField(max_length=200, blank=True, null=True)
    titleAr = models.CharField(max_length=200, blank=True, null=True)
    desEn = models.CharField(max_length=5000, blank=True, null=True)
    desAr = models.CharField(max_length=5000, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.titleEn)

class custodytype(models.Model):
    enName = models.CharField(max_length=200, blank=True, null=True)
    arName = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.enName)

class brands(models.Model):
    enName = models.CharField(max_length=200, blank=True, null=True)
    arName = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.enName)


class brandModel(models.Model):
    custodytype = models.ForeignKey(custodytype,on_delete=models.CASCADE)
    brand = models.ForeignKey(brands,on_delete=models.CASCADE)
    arName = models.CharField(max_length=250,blank=True,null=True)
    enName = models.CharField(max_length=250,blank=True,null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.enName)

class Building(models.Model):
    buildingName = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    Address = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.buildingName)


class Floor(models.Model):
    title = models.CharField(max_length=250)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Department(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, blank=True, null=True)
    titalAR = models.CharField(max_length=250, blank=True, null=True)
    belong = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class JobPosition(models.Model):
    title = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)


class Model(models.Model):
    title = models.CharField(max_length=250)


class Field(models.Model):
    title = models.CharField(max_length=250)


class ContractType(models.Model):
    title = models.CharField(max_length=250)
    titleAr = models.CharField(max_length=250)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    CompanyGOSIForSaudi = models.FloatField()
    CompanyGOSIForNonSaudi = models.FloatField()
    def __str__(self):
        return "{}".format(self.title)



gender_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class Employees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Working_Address = models.ForeignKey(location,on_delete=models.CASCADE)
    Work_Location = models.CharField(max_length=250)
    Work_Email = models.EmailField()
    Work_Mobile = models.CharField(max_length=250)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Job_position = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    Manager = models.CharField(max_length=250)
    Coach = models.CharField(max_length=250)
    Working_hours = models.CharField(max_length=250)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    isHr = models.BooleanField(blank=True,null=True)
    isManager = models.BooleanField(blank=True,null=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=250, choices=gender_CHOICE)
    nationalid = models.CharField(max_length=250, null=True, blank=True)
    employeenumber = models.CharField(max_length=250, null=True, blank=True)
    nationality = models.CharField(max_length=250, null=True, blank=True)
    DOJ = models.DateField(max_length=250, null=True, blank=True)
    idtype = models.CharField(max_length=250, null=True, blank=True)
    Work_Phone = models.BigIntegerField()
    grade = models.ForeignKey(EmployementGrades, on_delete=models.CASCADE,blank=True,null=True)
    level = models.ForeignKey(EmployementLevel, on_delete=models.CASCADE,blank=True,null=True)
    ccenter =models.ForeignKey(costcenter,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return "{}".format(self.user)


leavestatus_CHOICE = (
    ("1", "Pending"),
    ("2", "Approved"),
    ("3", "Rejected"),
)


class LeaveType(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    Title = models.CharField(max_length=500, blank=True, null=True)
    Override = models.BooleanField()
    Limit = models.IntegerField()
    ArTitle = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.Title)


class LeavesRequest(models.Model):
    Description = models.CharField(max_length=250, blank=True, null=True)
    Leave_Type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, blank=True, null=True)
    Duration_From = models.DateTimeField(default=timezone.now)
    Duration_To = models.DateTimeField(default=timezone.now)
    Duration_Days = models.CharField(max_length=250, blank=True, null=True)
    Reported_in_last_payslips = models.CharField(max_length=250, blank=True, null=True)
    CommentbyManager = models.CharField(max_length=5000, blank=True, null=True)
    user = models.ForeignKey(Employees, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=500, choices=leavestatus_CHOICE, default='Pending')

    def __str__(self):
        return "{}".format(self.user)


class InsuranceRenewals(models.Model):
    Model = models.ForeignKey(Model, on_delete=models.CASCADE)
    Search_by = models.CharField(max_length=250)
    Start_Date = models.DateField(default=timezone.now)
    End_Date = models.DateField(default=timezone.now)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Field = models.ForeignKey(Field, on_delete=models.CASCADE)
    Remainder_Before = models.IntegerField()
    Remainder_Expiry_Date = models.DateField(default=timezone.now)
    Active = models.BooleanField()


class SalaryStructures(models.Model):
    Name = models.CharField(max_length=250)
    Parent = models.CharField(max_length=250)
    Salary_Advance_After_Days = models.IntegerField()
    Reference = models.CharField(max_length=250)
    Max_Salary_Advance_Percentage = models.IntegerField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)


Stage_CHOICE = (
    ("1", "New"),
    ("2", "Running"),
    ("3", "To Renew"),
    ("4", "Expired"),
    ("5", "Cancelled"),
)

Type_CHOICE = (
    ("Full Time", "Full Time"),
    ("Contract Basis", "Contract Basis"),
)


class CreateContracts(models.Model):
    ContractsReference = models.CharField(max_length=250)
    Employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    Contract_Type = models.CharField(max_length=250, choices=Type_CHOICE)
    Date_From = models.DateField(default=timezone.now)
    Date_To = models.DateField(default=timezone.now)
    Stage = models.CharField(max_length=250, choices=Stage_CHOICE)
    base_salary = models.IntegerField(default=0,blank=True,null=True)
    Housing_Allowance = models.IntegerField(default=0,blank=True,null=True)
    Transport_Allowance = models.IntegerField(default=0,blank=True,null=True)
    GOSI = models.IntegerField(default=0)
    shift_start = models.TimeField()
    shift_end = models.TimeField()
    workinghours = models.IntegerField(default=0)
    breakhours = models.IntegerField(default=0)
    employment_type = models.CharField(max_length=250)
    contract_period = models.CharField(max_length=250)
    notice_period = models.CharField(max_length=250)
    probation_period = models.CharField(max_length=250)
    otherallowance = models.IntegerField(max_length=250,blank=True,null=True)
    allowance = models.ManyToManyField(allowances)

    def __str__(self):
        return "{}".format(self.ContractsReference)


conditionbased_CHOICE = (
    ("1", ""),
    ("2", "Other"),
)
amounttype_CHOICE = (
    ("1", "Fixed Amount"),
    ("2", "Other"),
)


class SalaryRules(models.Model):
    Name = models.CharField(max_length=250)
    Category = models.CharField(max_length=250)
    Code = models.CharField(max_length=250)
    Active = models.BooleanField(default=False)
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Sequence = models.IntegerField()
    AppearsOnPayslip = models.BooleanField(default=False)
    ConditionBasedOn = models.CharField(max_length=300, choices=conditionbased_CHOICE)
    AmountType = models.CharField(max_length=300, choices=amounttype_CHOICE)
    Quantity = models.IntegerField()
    FixedAmount = models.IntegerField()
    Contribution_Register = models.CharField(max_length=250)


class PayslipBatch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    Period_From = models.DateTimeField(default=datetime.now)
    Period_To = models.DateTimeField(default=datetime.now)
    PaySlip_Name = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.PaySlip_Name)


class EmployeePayslip(models.Model):
    Employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    PaySlip_Name = models.ForeignKey(PayslipBatch, on_delete=models.CASCADE)
    addition = models.IntegerField()
    no_of_working_hours = models.CharField(max_length=250)
    tax = models.CharField(max_length=250)
    other_deductions = models.CharField(max_length=250)
    earnings_as_per_workinghours = models.CharField(max_length=250)
    total_earnings = models.CharField(max_length=250)

    def __str__(self):
        return "{}".format(self.Employee)


class Announcements(models.Model):
    is_general_announcements = models.BooleanField(default=False, blank=True, null=True)
    code_no = models.CharField(max_length=250)
    title = models.CharField(max_length=5000)
    requestedDate = models.DateField(default=timezone.now)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    letter = models.CharField(max_length=10000)

    def __str__(self):
        return "{}".format(self.title)


class Plan(models.Model):
    manager = models.BooleanField(default=False)
    employee = models.BooleanField(default=False)
    collaborators = models.BooleanField(default=False)
    colleague = models.BooleanField(default=False)


class Appraisal(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    appraisal_deadline = models.DateField(default=timezone.now)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.employee)


ansType_CHOICE = (
    ("1", "Manually"),
    ("2", "Automatically"),
)
status_CHOICE = (
    ("1", "Completed"),
    ("2", "Partially Completed"),
    ("3", "Not Started Yet"),
)


class AnswerAppraisal(models.Model):
    survey = models.BooleanField(default=False)
    creationDate = models.DateField(default=timezone.now)
    deadline = models.DateField(default=timezone.now)
    partner = models.CharField(max_length=250)
    email = models.EmailField()
    answerType = models.CharField(max_length=250, choices=ansType_CHOICE)
    status = models.CharField(max_length=250, choices=status_CHOICE)

    def __str__(self):
        return "{}".format(self.status)


title_CHOICE = (
    ("1", "Mr."),
    ("2", "Ms."),
    ("3", "Mrs.")
)
language_CHOICE = (
    ("1", "English"),
    ("2", "Urdu"),
    ("3", "other"),
)


class Contact(models.Model):
    name = models.CharField(max_length=300)
    companyContact = models.ForeignKey(Company, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=5000)
    address2 = models.CharField(max_length=5000)
    pincode = models.IntegerField()
    country = models.CharField(max_length=5000)
    tin = models.IntegerField()
    # tags = models.TagField()
    jobPosition = models.CharField(max_length=500)
    phone = models.CharField(max_length=150)
    mobile = models.CharField(max_length=150)
    email = models.EmailField()
    website = models.URLField()
    title = models.CharField(max_length=250, choices=title_CHOICE)
    language = models.CharField(max_length=250, choices=language_CHOICE)

    def __str__(self):
        return "{}".format(self.companyContact)


ParentCat_Choice = (
    ("1", "Manufacturer"),
    ("2", "Other"),
)


class ContactTags(models.Model):
    tagName = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    parentCategory = models.CharField(max_length=250, choices=ParentCat_Choice)

    def __str__(self):
        return "{}".format(self.tagName)


class contactTitles(models.Model):
    title = models.CharField(max_length=500)
    abbreviation = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.title)


class ContactIndustry(models.Model):
    industryName = models.CharField(max_length=500)
    fullName = models.CharField(max_length=500)
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.industryName)


class createBanks(models.Model):
    BankName = models.CharField(max_length=500)
    BankIdentifierCode = models.CharField(max_length=500)
    address1 = models.CharField(max_length=500)
    address2 = models.CharField(max_length=500)
    pincode = models.IntegerField()
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    phone = models.IntegerField()
    email = models.EmailField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.BankName)


class CreateBankAC(models.Model):
    accountNo = models.CharField(max_length=5000)
    bank = models.ForeignKey(createBanks, on_delete=models.CASCADE)
    ABA_Routing = models.CharField(max_length=5000)
    currency = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.accountNo)


class createPublicChannel(models.Model):
    channelName = models.CharField(max_length=500)
    SendMessagesByEmail = models.BooleanField(default=False)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return "{}".format(self.channelName)


class allowanceToGrant(models.Model):
    Everyone = models.BooleanField(default=False)
    SelectedListOfUsers = models.BooleanField(default=False)
    PeopleHavingSomeBadges = models.BooleanField(default=False)
    NoOneAssignedThroughChallenges = models.BooleanField(default=False)


class CreateBadges(models.Model):
    BadgeTitle = models.CharField(max_length=500)
    Description = models.CharField(max_length=5000)
    AllownaceToGrant = models.ForeignKey(allowanceToGrant, on_delete=models.CASCADE)
    MonthlyLimitedSending = models.BooleanField(default=False)
    MyMonthlySendingTotal = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.BadgeTitle)


Periodicity_CHOICE = (
    ("1", "daily"),
    ("2", "Other"),
)


class DisplayMode(models.Model):
    IndividualGoals = models.BooleanField(default=False)
    LeaderBoard = models.BooleanField(default=False)


class CreateChallenge(models.Model):
    ChallengeName = models.CharField(max_length=500)
    AssignChallengeTo = models.CharField(max_length=500)
    Periodicity = models.CharField(max_length=500, choices=Periodicity_CHOICE)
    DisplayMode = models.ForeignKey(DisplayMode, on_delete=models.CASCADE)
    Responsible = models.ForeignKey(Employees, on_delete=models.CASCADE)
    StartDate = models.DateField()
    EndDate = models.DateField()

    def __str__(self):
        return "{}".format(self.ChallengeName)


Project_priority = (
    ("Low", "Low"),
    ("Medium", "Medium"),
    ("High", "High")
)


class Project(models.Model):
    Name = models.CharField(max_length=500)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Description = models.CharField(max_length=5000)
    Manager = models.ForeignKey(Employees, on_delete=models.CASCADE)
    Reference = models.CharField(max_length=500)
    Priority = models.CharField(max_length=500, choices=Project_priority)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.Name)


class RequestSalaryLetter(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return "{}".format(self.title)
