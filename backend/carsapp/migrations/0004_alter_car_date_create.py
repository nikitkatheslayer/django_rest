# Generated by Django 4.0.10 on 2023-07-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsapp', '0003_alter_car_brand_alter_car_date_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date_create',
            field=models.CharField(max_length=10, verbose_name='Дата производства'),
        ),
    ]
