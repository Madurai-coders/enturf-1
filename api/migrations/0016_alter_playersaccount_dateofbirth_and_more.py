# Generated by Django 4.0.6 on 2022-10-20 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_adminsettings_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersaccount',
            name='dateOfBirth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='playersaccount',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
