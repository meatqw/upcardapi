# Generated by Django 4.1.7 on 2023-06-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_alter_card_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='dob',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Дата рождения'),
        ),
    ]
