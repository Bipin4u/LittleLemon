# Generated by Django 5.0.6 on 2024-08-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_remove_booking_guest_number_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
