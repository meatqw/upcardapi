from django.db import models


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
    date_update = models.DateTimeField('Дата обновления', auto_now_add=True)

    def __str__(self):
        return self.purpose

    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображение'
