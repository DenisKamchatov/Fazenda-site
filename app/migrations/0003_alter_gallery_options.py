# Generated by Django 3.2.5 on 2021-08-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]