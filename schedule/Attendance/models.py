from django.db import models
from  home.models import Project
from django.contrib.auth.models import User

class Timesheet(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    Start = models.DateTimeField()
    End = models.DateTimeField(null=True)
    Description = models.CharField(max_length=5000)
    Remarks = models.CharField(max_length=5000,null=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return "{}".format(self.user)
