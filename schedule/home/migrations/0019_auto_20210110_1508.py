# Generated by Django 3.1.4 on 2021-01-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210110_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavetype',
            name='Override',
            field=models.BooleanField(default=False),
        ),
    ]
