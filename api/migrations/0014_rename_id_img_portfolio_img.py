# Generated by Django 4.1.7 on 2023-04-06 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_portfolio_id_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='id_img',
            new_name='img',
        ),
    ]