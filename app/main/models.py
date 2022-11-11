from django.db import models


class Artiles(models.Model):
    objects = None
    tittle = models.CharField('Название', max_length=20)
    mod = models.CharField('Модель', max_length=20)
    maxg = models.IntegerField('макс. груз')
    ves = models.IntegerField('Текущий вес')
    FE = models.IntegerField('FE,%', default=0)
    SiO2 = models.IntegerField('SiO2,%', default=0)
    koor = models.IntegerField('Координата', default=0)

    def __str__(self):
        return self.tittle

