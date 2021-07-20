from django.db import models
from django.template.defaultfilters import truncatewords
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='article_photos/%Y/%m/%d/', verbose_name='Фото')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    @property
    def short_description(self):
        return truncatewords(self.content, 20)

    def get_absolute_url(self):
        return reverse('article', kwargs={'article_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create']
