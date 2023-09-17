from django.db import models
from .account import Account


class Payment(models.Model):
    """Оплата"""

    STATUS = (
        ('NEW', 'Новый платеж'),
        ('CONFIRMED', 'Платеж подтвержден'),
        ('CANCELED', 'Платеж отменен'),
        ('FAIL', 'Ошибка')
    )

    payment_id = models.CharField(max_length=288)
    status = models.CharField(max_length=20, choices=STATUS)
    account_id = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    payment_url = models.CharField(max_length=288)
    amount = models.FloatField()
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.payment_id

    class Meta:
        verbose_name = 'Оплаты'
        verbose_name_plural = 'Оплаты'
