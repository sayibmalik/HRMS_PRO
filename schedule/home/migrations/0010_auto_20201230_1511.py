# Generated by Django 3.1.4 on 2020-12-30 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201229_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='Company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Company'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='Company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Company'),
        ),
    ]
