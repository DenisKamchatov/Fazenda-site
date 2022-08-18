# Generated by Django 3.2.5 on 2021-08-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_gallery_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='photo_webm',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография.webm'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография.jpg'),
        ),
    ]