# Generated by Django 4.0.6 on 2022-09-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
