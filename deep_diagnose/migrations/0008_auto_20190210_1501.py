# Generated by Django 2.1.5 on 2019-02-10 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deep_diagnose', '0007_auto_20190210_1458'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='AdminLogin',
        ),
        migrations.DeleteModel(
            name='CompanyLogin',
        ),
        migrations.DeleteModel(
            name='Services',
        ),
    ]
