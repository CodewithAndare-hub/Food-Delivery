# Generated by Django 5.0.6 on 2024-07-05 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_ordermodel_area_ordermodel_county_ordermodel_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='created_on',
        ),
    ]