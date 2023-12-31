# Generated by Django 4.2.4 on 2023-09-05 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200, verbose_name='Производитель')),
                ('model', models.CharField(max_length=200, verbose_name='Модель')),
                ('car_body', models.CharField(blank=True, max_length=100, null=True, verbose_name='Кузов')),
                ('odometer', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Пробег')),
                ('fuel_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Тип топлива')),
                ('car_volume', models.CharField(blank=True, max_length=20, null=True, verbose_name='Объем')),
                ('year', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Год')),
                ('gearbox', models.CharField(blank=True, max_length=20, null=True, verbose_name='Коробка передач')),
                ('drive_unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='Привод')),
                ('vin', models.CharField(blank=True, max_length=200, null=True, verbose_name='VIN')),
            ],
            options={
                'verbose_name': 'Авто в наличии',
                'verbose_name_plural': 'Авто в наличии',
            },
        ),
        migrations.CreateModel(
            name='CarInStockImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars_images/', verbose_name='Фотография')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_images', to='cars.car', verbose_name='Автомобиль')),
            ],
        ),
    ]
