from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        max_length=400,
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to='logo/',
        verbose_name="Логотип"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона"
    )
    address = models.CharField(
        max_length=300,
        verbose_name="Адрес"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class News(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='news_images/',
        verbose_name="Логотип"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"