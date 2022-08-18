from django.db import models
from django.db.models.base import Model


class Cottage(models.Model):
    title = models.CharField("Название", max_length=100)
    about = models.TextField('Описание')
    weekday = models.TextField('Будни')
    weekend_friday = models.TextField('Пятница')
    weekend_saturday = models.TextField('Суббота')
    new_year = models.TextField('Новый год')
    pre_new_year_weekday = models.TextField('Предновогодние будни')
    pre_new_year_weekend = models.TextField('Предновогодние выходные')
    postscript = models.CharField("Приписка", max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коттедж'
        verbose_name_plural = 'Коттеджи'


class Gallery(models.Model):

    photo = models.ImageField('Фотография.jpg', upload_to='photos/%Y/%m/%d/', null=True)
    photo_webp = models.ImageField('Фотография.webp', upload_to='photos/%Y/%m/%d/', null=True)
    cottage = models.ForeignKey(Cottage, on_delete=models.CASCADE, related_name='Коттедж')

    def __str__(self):
        return 'Фотография'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Contacts(models.Model):
    number = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return 'Номер телефона'

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'


class Photogallery(models.Model):
    photo = models.ImageField('Фотогалерея', upload_to='photogallery/%Y/%m/%d/', null=True)

    def __str__(self):
        return 'Фотогалерея'

    class Meta:
        verbose_name = 'Фотогалерея'
        verbose_name_plural = 'Фотогалерея'