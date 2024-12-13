# Generated by Django 3.2.3 on 2021-06-21 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0087_holidays'),
    ]

    operations = [
        migrations.CreateModel(
            name='costcenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameAR', models.CharField(blank=True, max_length=250, null=True)),
                ('nameEN', models.CharField(blank=True, max_length=250, null=True)),
                ('desAR', models.CharField(blank=True, max_length=5000, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.company')),
            ],
        ),
    ]
