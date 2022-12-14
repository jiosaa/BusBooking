# Generated by Django 4.0.6 on 2022-09-13 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Booker', '0001_initial'),
        ('Bus_admin', '0001_initial'),
        ('System_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentinformation',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='System_admin.paymentmethod'),
        ),
        migrations.AddField(
            model_name='paymentinformation',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bus_admin.route'),
        ),
        migrations.AddField(
            model_name='finishpayment',
            name='payment_method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booker.paymentinformation'),
        ),
    ]
