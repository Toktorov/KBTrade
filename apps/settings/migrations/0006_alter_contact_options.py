# Generated by Django 4.2.4 on 2023-09-23 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_setting_cars_setting_logistics_setting_spare_parts_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Заявки на подбор', 'verbose_name_plural': 'Заявки на подбор'},
        ),
    ]
