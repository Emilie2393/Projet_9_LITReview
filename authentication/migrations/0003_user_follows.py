# Generated by Django 4.2.7 on 2023-12-04 15:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follows',
            field=models.ManyToManyField(limit_choices_to={'role': 'SUBSCRIBER'}, to=settings.AUTH_USER_MODEL, verbose_name='suit'),
        ),
    ]
