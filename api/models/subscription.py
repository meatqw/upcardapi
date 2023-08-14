from django.db import models


class Subscription(models.Model):
    """Модель c подписками"""
    name = models.CharField(max_length=300, blank=True)
    price = models.IntegerField(null=False)
    data = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписка'
