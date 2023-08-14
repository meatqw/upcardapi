from django.db import models

from .social import Social


class CompanyInfo(models.Model):
    """Модель инфо о компании"""
    name = models.CharField('Наименование', max_length=250, blank=True)
    activity = models.CharField('Деятельность', max_length=250, blank=True)
    foundation = models.CharField('Год основания', max_length=250, blank=True)
    clientage = models.CharField('Клиенты', max_length=250, blank=True)
    phone = models.CharField('Телефон', max_length=250, blank=True)
    work_phone = models.CharField('Рабочий телефон', max_length=250, blank=True)
    company_site = models.CharField('Сайт компании', max_length=250, blank=True)
    fax = models.CharField('Факс', max_length=250, blank=True)
    email = models.CharField('Почта', max_length=250, blank=True)
    address = models.CharField('Адрес', max_length=250, blank=True)

    id_social = models.ForeignKey(Social, on_delete=models.SET_NULL, blank=True, null=True)
    logo_img = models.ImageField(upload_to="media/", null=True, blank=True)

    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфо о компании'
        verbose_name_plural = 'Инфо о компании'
