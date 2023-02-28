# Generated by Django 4.0.6 on 2022-10-26 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_playersaccount_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingreport',
            name='slotClosingTime',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AddField(
            model_name='bookingreport',
            name='slotOpeningTime',
            field=models.TimeField(default='00:00'),
        ),
        migrations.AlterField(
            model_name='bookingreport',
            name='bookingStatus',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('CL', 'CANCELED'), ('P', 'PENDING')], default='P', max_length=2),
        ),
    ]