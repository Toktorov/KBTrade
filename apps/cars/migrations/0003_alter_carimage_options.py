# Generated by Django 4.2.4 on 2023-09-05 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_rename_carinstockimage_carimage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carimage',
            options={'verbose_name': 'Картинка авто', 'verbose_name_plural': 'Картинки авто'},
        ),
    ]