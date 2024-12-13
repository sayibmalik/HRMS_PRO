# Generated by Django 3.2.3 on 2021-06-22 06:07

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0095_alter_location_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Working_Address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
    ]
