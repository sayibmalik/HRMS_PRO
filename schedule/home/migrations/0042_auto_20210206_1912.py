# Generated by Django 3.1.5 on 2021-02-06 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_createcontracts_otherallowance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslipbatch',
            name='Period_From',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='payslipbatch',
            name='Period_To',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
