# Generated by Django 4.1.7 on 2023-05-03 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_social_gmail_social_google'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300)),
                ('price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Подписка',
                'verbose_name_plural': 'Подписка',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='id_subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.subscription'),
        ),
    ]
