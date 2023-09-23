from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя"
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия"
    )
    user_id = models.CharField(
        max_length=100,
        verbose_name="USER ID"
    )
    phone_number = models.CharField(
        max_length=200,
        verbose_name="Номер телефонна",
        blank=True, null=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return self.username 
    
    class Meta:
        verbose_name = "Пользователь телеграмма"
        verbose_name_plural = "Пользователи телеграммов"