# Generated by Django 3.2.6 on 2021-08-25 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210825_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='photowebp',
            new_name='photo_webp',
        ),
    ]