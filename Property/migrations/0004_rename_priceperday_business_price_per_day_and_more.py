# Generated by Django 4.0.2 on 2022-02-14 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0003_remove_businessrooms_business_storage_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='pricePerDay',
            new_name='price_per_day',
        ),
        migrations.RenameField(
            model_name='climatecontrolled',
            old_name='pricePerDay',
            new_name='price_per_day',
        ),
        migrations.RenameField(
            model_name='garage',
            old_name='pricePerHour',
            new_name='price_per_hour',
        ),
        migrations.RenameField(
            model_name='personal',
            old_name='pricePerDay',
            new_name='price_per_day',
        ),
    ]