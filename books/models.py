from django.db import models

from authors.models import Authors

NULLABLE = {'blank': True, 'null': True}


class Books(models.Model):
    STATUS_CHOICES = [
        ('available', 'Доступна'),
        ('borrowed', 'Занята'),
        ('lost', 'Потеряна'),
    ]

    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ForeignKey(Authors, max_length=100, on_delete=models.CASCADE, verbose_name='Автор книги')
    written_date = models.DateTimeField(**NULLABLE, verbose_name='Дата написание книги')
    genre = models.CharField(max_length=100, verbose_name='Жанр книги')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='available', verbose_name='Статус книги')

