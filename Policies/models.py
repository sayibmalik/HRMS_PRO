from django.db import models
from home.models import Company,Employees
# Create your models here.
class policies(models.Model):
    titleAR = models.CharField(max_length=200,blank=True,null=True)
    titleEN = models.CharField(max_length=200,blank=True,null=True)
    file = models.FileField(blank=True,null=True)
    employee = models.ForeignKey(Employees,on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.titleEN)