# Generated by Django 4.0.6 on 2022-11-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_playersaccount_colorcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingreport',
            name='bookedAt',
            field=models.DateField(),
        ),
    ]
