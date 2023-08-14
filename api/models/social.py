from django.db import models


class Social(models.Model):
    """Модель для хранения соц сетей"""
    telegram = models.CharField(
        'telegram', max_length=250, blank=True, null=True)
    vk = models.CharField('vk', max_length=250, blank=True, null=True)
    instagram = models.CharField(
        'instagram', max_length=250, blank=True, null=True)
    whatsapp = models.CharField(
        'whatsapp', max_length=250, blank=True, null=True)
    google = models.CharField('google', max_length=250, blank=True, null=True)
    facebook = models.CharField(
        'facebook', max_length=250, blank=True, null=True)
    yandex = models.CharField('yandex', max_length=250, blank=True, null=True)
    odnoklassniki = models.CharField(
        'odnoklassniki', max_length=250, blank=True, null=True)
    skype = models.CharField('skype', max_length=250, blank=True, null=True)
    youtube = models.CharField(
        'youtube', max_length=250, blank=True, null=True)
    github = models.CharField('github', max_length=250, blank=True, null=True)
    behance = models.CharField(
        'behance', max_length=250, blank=True, null=True)
    tiktok = models.CharField('tiktok', max_length=250, blank=True, null=True)
    linkedin = models.CharField(
        'linkedin', max_length=250, blank=True, null=True)
    twitter = models.CharField(
        'twitter', max_length=250, blank=True, null=True)
    viber = models.CharField('viber', max_length=250, blank=True, null=True)
    twitch = models.CharField('twitch', max_length=250, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return f'{self.date_create}'

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'
