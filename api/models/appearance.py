from django.db import models


class Appearance(models.Model):
    """Модель внешного вида карточки"""
    name = models.CharField('Наименование', max_length=250, blank=True)
    style = models.JSONField('Стиль', blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайн карточек'
