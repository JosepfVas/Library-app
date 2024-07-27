from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Authors(models.Model):
    name = models.CharField(max_length=150, **NULLABLE, verbose_name='Имя писателя')
    surname = models.CharField(max_length=150, **NULLABLE, verbose_name='Фамилия писателя')
    date_of_birth = models.DateField(**NULLABLE, verbose_name='Дата рождения')
    date_of_death = models.DateField(**NULLABLE, verbose_name='Дата смерти')
    biography = models.TextField(**NULLABLE, verbose_name='Биография писателя')
