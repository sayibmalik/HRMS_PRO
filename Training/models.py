from django.db import models
from home.models import Company

# Create your models here.
class training(models.Model):
    AR_Title = models.CharField(max_length=200,blank=True,null=True)
    EN_Title = models.CharField(max_length=200,blank=True,null=True)
    AR_courceInstructions = models.CharField(max_length=200,blank=True,null=True)
    EN_courceInstructions = models.CharField(max_length=200,blank=True,null=True)
    startDate = models.DateField()
    courceDays = models.CharField(max_length=200,blank=True,null=True)
    website = models.URLField(blank=True,null=True)
    numberOfSeats = models.IntegerField(blank=True,null=True)
    AR_description = models.CharField(max_length=5000,blank=True,null=True)
    EN_description = models.CharField(max_length=5000,blank=True,null=True)
    address = models.CharField(max_length=5000,blank=True,null=True)
    company= models.ForeignKey(Company,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return "{}" .format(self.EN_Title)
