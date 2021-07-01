from django.db import models
from home.models import Employees,documentType
from django.contrib.auth.models import User
# Create your models here.

doctype_CHOICE =(
    ("Visa","Visa"),
    ("IDs","IDs"),
    ("Personal","Personal")
)

class Documents(models.Model):
    employee =  models.ForeignKey(Employees,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    doctype = models.ForeignKey(documentType,on_delete=models.CASCADE,blank=True,null=True)
    file = models.FileField()
    def __str__(self):
        return "{}" .format(self.title)

status_CHOICE =(
    ("Return","Return"),
    ("Active","Active"),

)

class Assets(models.Model):
    employee =  models.ForeignKey(Employees,on_delete=models.CASCADE)
    type = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    handover = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=status_CHOICE)
    returndate = models.DateField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "{}" .format(self.employee)


class notes(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    addedby = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.CharField(max_length=1000)

    def __str__(self):
        return "{}".format(self.employee)