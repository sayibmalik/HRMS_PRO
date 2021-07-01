from django.db import models
from home.models import Employees,Company
# Create your models here.
priority_CHOICE=[
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
]


class SupportTicket(models.Model):
    ticketNumber = models.CharField(max_length=200,blank=True,null=True)
    subject = models.CharField(max_length=2000,blank=True,null=True)
    priority = models.CharField(max_length=200,choices=priority_CHOICE,blank=True,null=True)
    status = models.DateTimeField(auto_now_add=True)
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE)
    description = models.CharField(max_length=5000,blank=True,null=True)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.subject)