from django.db import models


class Social(models.Model):
    """Модель для хранения соц сетей"""
    tg = models.CharField('tg', max_length=250, blank=True, null=True)
    vk = models.CharField('vk', max_length=250, blank=True, null=True)
    instagram = models.CharField('instagram', max_length=250, blank=True, null=True)
    whatsapp = models.CharField('whatsapp', max_length=250, blank=True, null=True)
    gmail = models.CharField('gmail', max_length=250, blank=True, null=True)
    facebook = models.CharField('facebook', max_length=250, blank=True, null=True)
    yandex = models.CharField('yandex', max_length=250, blank=True, null=True)
    odnoclassniki = models.CharField('odnoclassniki', max_length=250, blank=True, null=True)
    skype = models.CharField('skype', max_length=250, blank=True, null=True)
    youtube = models.CharField('youtube', max_length=250, blank=True, null=True)
    github = models.CharField('github', max_length=250, blank=True, null=True)
    beehance = models.CharField('beehance', max_length=250, blank=True, null=True)
    tiktok = models.CharField('tiktok', max_length=250, blank=True, null=True)
    linkedin = models.CharField('linkedin', max_length=250, blank=True, null=True)
    twitter = models.CharField('twitter', max_length=250, blank=True, null=True)
    viber = models.CharField('viber', max_length=250, blank=True, null=True)
    twitch = models.CharField('twitch', max_length=250, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.date_create}'

    class Meta:
        verbose_name = 'Соц сеть'
        verbose_name_plural = 'Соц сети'


class Appearance(models.Model):
    """Модель внешного вида карточки"""
    name = models.CharField('Наименование', max_length=250, blank=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайн карточек'
        

class Account(models.Model):
    """Модель аккаунта"""
    email = models.CharField('Почта', max_length=250, blank=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


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
    id_card = models.ForeignKey(Appearance, on_delete=models.SET_NULL, blank=True, null=True)

    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инфо о компании'
        verbose_name_plural = 'Инфо о компании'
        
class Card(models.Model):
    """Модель карточки"""
    card_name = models.CharField('Наименование карточки', max_length=250, blank=True)
    name = models.CharField('Имя', max_length=250, blank=True)
    surname = models.CharField('Фамилия', max_length=250, blank=True)
    patronymic = models.CharField('Отчество', max_length=250, blank=True)
    spec = models.CharField('Специализация', max_length=250, blank=True)
    phone = models.CharField('Телефон', max_length=250, blank=True)
    home_phone = models.CharField('Домашний телефон', max_length=250, blank=True)
    personal_site = models.CharField('Сайт', max_length=250, blank=True)
    email = models.CharField('Почта', max_length=250, blank=True)
    dob = models.DateTimeField('Дата рождения', auto_now_add=True)
    address = models.CharField('Адрес', max_length=250, blank=True)
    qr = models.CharField('QR', max_length=250, blank=True)
    
    personal_pic = models.ImageField(upload_to="media/")
    logo_pic = models.ImageField(upload_to="media/")
    
    id_social = models.ForeignKey(Social, on_delete=models.SET_NULL, blank=True, null=True)
    id_appearance = models.ForeignKey(Appearance, on_delete=models.SET_NULL, blank=True, null=True)
    id_account = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)

    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'
        

class Portfolio(models.Model):
    """Модель портфолио"""
    name = models.CharField('Почта', max_length=250, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)
    description = models.CharField('Описание', max_length=250, blank=True, null=True)
    
    pic = models.ImageField(upload_to="media/")
    
    id_card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'
        
        
class Calendar(models.Model):
    """Модель кальндаря"""
    id_card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Календарь'
        verbose_name_plural = 'Календарь'