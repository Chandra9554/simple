# Generated by Django 3.0.2 on 2020-08-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200807_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_info',
            name='Date_of_joining',
            field=models.DateField(),
        ),
    ]
