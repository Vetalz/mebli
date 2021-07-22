from django.db import models


class Gallery_peretyazhka(models.Model):
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


class Clients_peretyazhka(models.Model):
    number_phone = models.CharField(max_length=13, verbose_name='Номер телефона')
    name = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self):
        return self.number_phone

    class Meta:
        verbose_name = 'Клиента'
        verbose_name_plural = 'Клиенты'

