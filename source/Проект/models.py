from django.db import models

# Create your models here.
from Организация.models import Организация

class Проект(models.Model):
    наименование_устройства = models.CharField(max_length=100)
    краткое_наименование = models.CharField(max_length=20, blank=True, null=True)
    шифр = models.CharField(max_length=100)
    код = models.CharField(max_length=20, blank=True, null=True)

    заказчик = models.ForeignKey(Организация, on_delete=models.PROTECT, null=True,)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return str(self.наименование_устройства)
