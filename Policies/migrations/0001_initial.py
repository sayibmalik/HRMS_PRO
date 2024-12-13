# Generated by Django 3.2.11 on 2024-12-11 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='policies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleAR', models.CharField(blank=True, max_length=200, null=True)),
                ('titleEN', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.employees')),
            ],
        ),
    ]
