# Generated by Django 4.2.4 on 2023-09-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Цвет'),
        ),
    ]
