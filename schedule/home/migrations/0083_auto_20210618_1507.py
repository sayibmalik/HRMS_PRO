# Generated by Django 3.2.3 on 2021-06-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0082_employees_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='blonge',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='titalAR',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
