# Generated by Django 5.0.6 on 2024-07-04 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(upload_to='menuitem_images'),
        ),
    ]