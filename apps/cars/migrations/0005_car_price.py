# Generated by Django 4.2.4 on 2023-09-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Цена'),
        ),
    ]