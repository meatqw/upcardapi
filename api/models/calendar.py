from django.db import models

from .card import Card


class Calendar(models.Model):
    """Модель кальндаря"""
    id_card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календарь'
