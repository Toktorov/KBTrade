# Generated by Django 4.2.4 on 2023-09-05 17:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarInStockImage',
            new_name='CarImage',
        ),
        migrations.AlterModelOptions(
            name='carimage',
            options={'verbose_name': 'Картинки авто'},
        ),
        migrations.AddField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
    ]