# Generated by Django 3.2.5 on 2021-08-25 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_photogallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photogallery',
            options={'verbose_name': 'Фотогалерея', 'verbose_name_plural': 'Фотогалерея'},
        ),
        migrations.RenameField(
            model_name='gallery',
            old_name='photo_webp',
            new_name='photowebp',
        ),
    ]