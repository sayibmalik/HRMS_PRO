# Generated by Django 3.1.2 on 2021-02-06 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20210206_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='DOJ',
            field=models.DateField(max_length=250),
        ),
    ]
