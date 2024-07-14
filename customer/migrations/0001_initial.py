# Generated by Django 5.0.6 on 2024-07-04 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=100)),
                ('image', models.ImageField(default='', height_field=200, upload_to='menu_images', width_field=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.ManyToManyField(related_name='item', to='customer.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('items', models.ManyToManyField(blank=True, related_name='order', to='customer.menuitem')),
            ],
        ),
    ]
