# Generated by Django 3.2.3 on 2021-06-14 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0070_alter_employees_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employementgrades',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.jobtitle'),
        ),
        migrations.AlterField(
            model_name='employementlevel',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employementgrades'),
        ),
    ]
