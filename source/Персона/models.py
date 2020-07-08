from django.db import models

# Create your models here.
from Адрес.models import Адрес 

class Персона(models.Model):
    ФИО = models.CharField(max_length=100)
    телефон = models.CharField(max_length=10)
    email = models.EmailField()
    инн = models.CharField(max_length=100)

    серия = models.CharField(max_length=10)
    номер = models.CharField(max_length=20)
    кем_выдан = models.CharField(max_length=100)
    код_подразделения = models.CharField(max_length=100)
    дата_выдачи = models.DateField()
    место_регистрации = models.ForeignKey(Адрес, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Персона'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return str(self.ФИО)
