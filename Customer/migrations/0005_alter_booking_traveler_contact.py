# Generated by Django 4.0.6 on 2022-09-08 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0004_alter_booking_traveler_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='traveler_contact',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
