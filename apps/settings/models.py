from django.db import models

# Create your models here.

class Settings(models.Model):
    title = models.CharField(
        max_length=30,
        verbose_name="Названия сайта"
    )
    descriptions = models.TextField(
        verbose_name="Описания сайта"
    )
    logo = models.ImageField(
        upload_to="logo/",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=30,
        verbose_name="Телефонный номер",
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Ваша почта",
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Ваш адресс",
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name="Ваш Instagram",
        blank=True, null=True
    )
    fasebook = models.URLField(
        verbose_name="Ваш Fasebook",
        blank=True, null=True
    )
    youtube = models.URLField(
        verbose_name="Ваш youtube",
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка",
        verbose_name_plural = 'Настройки'    

class Abaut(models.Model):    
    description = models.TextField(
        verbose_name="Наша история",
        blank=True, null=True
    )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "О нас",
        verbose_name_plural = 'О нас' 



