from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=64, verbose_name='Марка')
    model = models.CharField(max_length=64, verbose_name='Модель')
    date_create = models.CharField(max_length=10, verbose_name='Дата производства', blank=True, null=True)

    def __str__(self):
        return f'{self.brand} {self.model}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

