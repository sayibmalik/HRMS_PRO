from django.db import models
from django.contrib.auth.models import User
from home.models import Company

# Create your models here.
class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    Description = models.CharField(max_length=5000)
    Immidiate=models.BooleanField(default=False)
    Is_Featured=models.BooleanField(default=False)
    Is_Published=models.BooleanField(default=False)
    def __str__(self):
        return "{}" .format(self.title)

class Resumes(models.Model):
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    CV = models.FileField()
    def __str__(self):
        return "{}" .format(self.job)
