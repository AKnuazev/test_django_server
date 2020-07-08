from django.db import models

# Create your models here.
from Разрешение.models import Разрешение

class Организация(models.Model):
    наименование=models.CharField(max_length=100)
    директор=models.CharField(max_length=100)
    руководитель=models.CharField(max_length=100)
    исполнитель=models.CharField(max_length=100)
    согласователь=models.CharField(max_length=100)

    разрешения=models.ManyToManyField(Разрешение)  # Убрали разрешение -> убираем его у всех организаций

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return str(self.наименование)
    