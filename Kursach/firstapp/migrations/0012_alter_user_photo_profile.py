# Generated by Django 3.2.8 on 2021-12-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_user_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo_profile',
            field=models.ImageField(blank=True, upload_to='photos_profile/%Y/%m/%d', verbose_name='Фото профиля'),
        ),
    ]
