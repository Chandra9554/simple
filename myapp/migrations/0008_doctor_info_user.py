# Generated by Django 3.0.2 on 2020-08-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200808_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_info',
            name='user',
            field=models.CharField(default='', max_length=50),
        ),
    ]