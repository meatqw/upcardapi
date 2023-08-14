from django.db import models

from .account import Account
from .subscription import Subscription


class UserSubscribe(models.Model):
    card_count = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    id_account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    id_subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.id_account.email

    class Meta:
        verbose_name = 'Подписки пользователя'
        verbose_name_plural = 'Подписка пользователя'
