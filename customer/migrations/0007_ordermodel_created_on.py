# Generated by Django 5.0.6 on 2024-07-06 05:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_remove_ordermodel_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]