from django.db import models

# Create your models here.
class Car(models.Model):
    make = models.CharField(
        max_length=200,
        verbose_name="Производитель"
    )
    model = models.CharField(
        max_length=200,
        verbose_name="Модель"
    )
    car_body = models.CharField(
        max_length=100,
        verbose_name="Кузов",
        blank=True, null=True
    )
    odometer = models.PositiveSmallIntegerField(
        verbose_name="Пробег",
        blank=True, null=True
    )
    fuel_type = models.CharField(
        max_length=100,
        verbose_name="Тип топлива",
        blank=True, null=True
    )
    car_volume = models.CharField(
        max_length=20,
        verbose_name="Объем",
        blank=True, null=True
    )
    year = models.PositiveSmallIntegerField(
        verbose_name="Год",
        blank=True, null=True
    )
    gearbox = models.CharField(
        max_length=20,
        verbose_name="Коробка передач",
        blank=True, null=True
    )
    drive_unit = models.CharField(
        max_length=50,
        verbose_name="Привод",
        blank=True, null=True
    )
    vin = models.CharField(
        max_length=200,
        verbose_name="VIN",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.make} {self.model}"
    
    class Meta:
        verbose_name = "Авто в наличии"
        verbose_name_plural = "Авто в наличии"

class CarImage(models.Model):
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE,
        related_name='car_images',
        verbose_name="Автомобиль"
    )
    image = models.ImageField(
        upload_to='cars_images/',
        verbose_name="Фотография"
    )

    def __str__(self):
        return f"{self.car} {self.image}"
    
    class Meta:
        verbose_name = 'Картинка авто'
        verbose_name_plural = 'Картинки авто'