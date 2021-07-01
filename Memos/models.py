from django.db import models
from home.models import Employees,Department,Company
import datetime
# Create your models here.
notificationicon_CHOICE=[
    ("Info","Info"),
    ("Check","Check"),
    ("Warning","Warning"),
    ("Danger","Danger"),
]

class memos(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    notificationIcon = models.CharField(max_length=50,choices=notificationicon_CHOICE,blank=True,null=True)
    titleAR = models.CharField(max_length=500,blank=True,null=True)
    titleEN = models.CharField(max_length=500,blank=True,null=True)
    bodyAR = models.CharField(max_length=5000,blank=True,null=True)
    bodyEN = models.CharField(max_length=5000,blank=True,null=True)
    file = models.FileField(blank=True,null=True,upload_to='media/')
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    def __str__(self):
        return "{}".format(self.titleEN)

