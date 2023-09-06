from django.db import models
from django_resized.forms import ResizedImageField

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
    facebook = models.URLField(
        verbose_name="Facebook",
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name="Instagram",
        blank=True, null=True
    )
    tiktok = models.URLField(
        verbose_name="TikTok",
        blank=True, null=True
    )
    whatsapp = models.URLField(
        verbose_name="WhatsApp",
        blank=True, null=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата заявки"
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Review(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя"
    )
    text = models.TextField(
        max_length=400,
        verbose_name="Отзыв"
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class News(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='news_images/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Benefit(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        max_length=400,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"

class Team(models.Model):
    name_surname = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    job_title = models.CharField(
        max_length=100,
        verbose_name="Должность"
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='teams_images/',
        verbose_name="Фотография",
        blank = True, null = True
    )

    def __str__(self):
        return self.name_surname
    
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"