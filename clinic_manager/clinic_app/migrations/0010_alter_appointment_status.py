# Generated by Django 5.0.4 on 2024-05-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0009_alter_bill_zalopay_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('cancelled', 'Cancelled'), ('completed', 'Complete')], default='pending', max_length=20),
        ),
    ]
