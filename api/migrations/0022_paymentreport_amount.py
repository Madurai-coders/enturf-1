# Generated by Django 4.0.6 on 2022-11-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_bookingreport_bookedat'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentreport',
            name='amount',
            field=models.CharField(default=0, max_length=125),
        ),
    ]
