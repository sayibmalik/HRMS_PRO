from django.urls import path, include
from .views import employeePayslip, CreateEmployeePayslip, PayslipBatches, CreatePayslipBatch, salaryStructures, \
    CreateSalaryStructure, salaryRules, CreateSalaryRules , Editemployeepayslip, Delemployeepayslip,BatchEmp,\
    salaryslip,getdata
from django.conf.urls import url

urlpatterns = [
    path('employeepayslip/', employeePayslip, name='employeePayslip'),
    path('delemployeepayslip/', Delemployeepayslip, name='Delemployeepayslip'),
    url(r'^editemployeepayslip/(?P<pk>[0-9]+)/$',Editemployeepayslip , name='Editemployeepayslip'),
    url(r'^createemployeepayslip/(?P<pk>[0-9]+)/$', CreateEmployeePayslip, name='CreateEmployeePayslip'),
    path('payslipbatch/', PayslipBatches, name='PayslipBatch'),
    url(r'^BatchEmployees/(?P<pk>[0-9]+)/$', BatchEmp, name='BatchEmp'),
    url(r'^salaryslip/(?P<pk>[0-9]+)/$', salaryslip, name='salaryslip'),
    path('createpayslipbatch/', CreatePayslipBatch, name='CreatePayslipBatch'),
    path('salarystructures/', salaryStructures, name='salaryStructures'),
    path('createsalarystructure/', CreateSalaryStructure, name='CreateSalaryStructure'),
    path('salaryrules/', salaryRules, name='salaryRules'),
    path('createsalaryrules/', CreateSalaryRules, name='CreateSalaryRules'),
    path('getdata/', getdata, name='getdata')
]
