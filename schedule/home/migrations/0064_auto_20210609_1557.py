# Generated by Django 3.2.3 on 2021-06-09 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_alter_announcements_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcements',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='createbankac',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='jobposition',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='leavetype',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='payslipbatch',
            old_name='Company',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Company',
            new_name='company',
        ),
    ]
