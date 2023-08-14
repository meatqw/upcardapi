from django.db import models

from .account import Account
from .appearance import Appearance
from .company_info import CompanyInfo
from .social import Social


class Card(models.Model):
    """Модель карточки"""
    card_name = models.CharField('Наименование карточки', max_length=250, blank=True)
    name = models.CharField('Имя', max_length=250, blank=True)
    surname = models.CharField('Фамилия', max_length=250, blank=True)
    patronymic = models.CharField('Отчество', max_length=250, blank=True)
    spec = models.CharField('Специализация', max_length=250, blank=True)
    phone = models.CharField('Телефон', max_length=250, blank=True)
    personal_site = models.CharField('Сайт', max_length=250, blank=True)
    email = models.CharField('Почта', max_length=250, blank=True)
    address = models.CharField('Адрес', max_length=250, blank=True)
    link = models.CharField('link', max_length=250, blank=True)
    subcard = models.CharField('Подкарта', max_length=250, default='Портфолио', blank=True, null=True)

    personal_img = models.ImageField(upload_to="media/", null=True, blank=True)
    logo_img = models.ImageField(upload_to="media/", null=True, blank=True)

    id_company_info = models.ForeignKey(CompanyInfo, on_delete=models.SET_NULL, blank=True, null=True)
    id_social = models.ForeignKey(Social, on_delete=models.SET_NULL, blank=True, null=True)
    id_appearance = models.ForeignKey(Appearance, on_delete=models.SET_NULL, blank=True, null=True)
    id_account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)

    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
