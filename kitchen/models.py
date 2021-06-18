from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    budget = models.FloatField(blank=True, verbose_name='Бюджет', null=True)
    currency = models.CharField(max_length=5, default='UAH', verbose_name='Валюта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Clients(models.Model):
    number_phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    budget = models.FloatField(blank=True, verbose_name='Бюджет', null=True)
    real_budget = models.FloatField(blank=True, verbose_name='Фактический бюджет', null=True)
    phone_ring = models.BooleanField(default=False, verbose_name='Звонок')
    measuring = models.BooleanField(default=False, verbose_name='Замер')
    order = models.BooleanField(default=False, verbose_name='Заказ')
    currency = models.CharField(max_length=5, default='UAH', verbose_name='Валюта')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self):
        return self.number_phone

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'
