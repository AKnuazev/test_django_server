from django.db import models

# Create your models here.

from Адрес.models import Адрес

class Документ(models.Model):
    наименование=models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return str(self.наименование)

    
