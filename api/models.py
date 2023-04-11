from django.db import models
from django.contrib.auth.models import User
import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Image(models.Model):
    """Модель изображения"""
    
    PURPOSE = (
        ('CARD_PERSONAL_PIC', 'Персональное фото картчоки'),
        ('CARD_LOGO_PIC', 'Лого компании'),
        ('PORTFOLIO_PIC', 'Портфолио'),
        ('OTHER', 'Другое'),
    )
    
    img = models.ImageField(upload_to="media/")
    purpose = models.CharField(max_length=20, choices=PURPOSE)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)
    
    
    def __str__(self):
        return self.purpose

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображение'



class Social(models.Model):
    """Модель для хранения соц сетей"""
    telegram = models.CharField('telegram', max_length=250, blank=True, null=True)
    vk = models.CharField('vk', max_length=250, blank=True, null=True)
    instagram = models.CharField('instagram', max_length=250, blank=True, null=True)
    whatsapp = models.CharField('whatsapp', max_length=250, blank=True, null=True)
    gmail = models.CharField('gmail', max_length=250, blank=True, null=True)
    facebook = models.CharField('facebook', max_length=250, blank=True, null=True)
    yandex = models.CharField('yandex', max_length=250, blank=True, null=True)
    odnoklassniki = models.CharField('odnoklassniki', max_length=250, blank=True, null=True)
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
    style = models.JSONField('Стиль', blank=True, null=True)
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дизайн'
        verbose_name_plural = 'Дизайн карточек'
        


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def last_login(self):
        return None

    
        
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
    link = models.CharField('link', max_length=250, blank=True)
    
    # id_img = models.ManyToManyField(Image, blank=True)
    personal_img = models.ImageField(upload_to="media/", null=True, blank=True)
    logo_img = models.ImageField(upload_to="media/", null=True, blank=True)
    id_company_info = models.ForeignKey(CompanyInfo, on_delete=models.SET_NULL, blank=True, null=True)
    
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
    name = models.CharField('Название', max_length=250, blank=True)
    date = models.DateTimeField('Дата', auto_now_add=True)
    description = models.CharField('Описание', max_length=250, blank=True, null=True)
    
    img = models.ImageField(upload_to="media/", null=True, blank=True)
    id_card = models.ForeignKey(Card, on_delete=models.SET_NULL, blank=True, null=True)
    
    date_create = models.DateTimeField('Дата создания', auto_now_add=True)
    date_update =models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.name

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
        
        
