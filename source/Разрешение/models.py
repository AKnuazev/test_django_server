from django.db import models

# Create your models here.


class Разрешение(models.Model):
    типы = (
        ("1", "Лицензия"),
        ("2", "Свидетельство"),
        ("3", "Аттестат аккредитации"),
        ("4", "Сертификат соответствия"),
        ("5", "Санитарно-эпидемиологическое заключение"),
        ("6", "Экспертное заключение"),
        ("7", "СРО")
    )

    выбор_типа = models.CharField(max_length=1, choices=типы)
    серия_и_номер = models.CharField(max_length=20)
    кем_выдан = models.CharField(max_length=100)
    описание = models.TextField()
    дата_выдачи = models.DateField()
    срок_окончания = models.DateField()

    class Meta:
        verbose_name = 'Разрешение'
        verbose_name_plural = 'Разрешения'

    def __str__(self):
        return str(self.типы[int(self.выбор_типа) - 1][1])


# TODO: delete folowing test
типы = (
        ("1", "Лицензия"),
        ("2", "Свидетельство"),
        ("3", "Аттестат аккредитации"),
        ("4", "Сертификат соответствия"),
        ("5", "Санитарно-эпидемиологическое заключение"),
        ("6", "Экспертное заключение"),
        ("7", "СРО")
    )
выбор_типа=1

print(str(типы[выбор_типа - 1][1]))