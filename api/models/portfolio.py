from django.db import models

from .card import Card


class Portfolio(models.Model):
    """Модель портфолио"""
    name = models.CharField('Название', max_length=250, blank=True)
    date = models.CharField('Подзаголовок', max_length=250)
    description = models.CharField('Описание', max_length=250, blank=True, null=True)

    img = models.ImageField(upload_to="media/", null=True, blank=True)
    id_card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)

    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
