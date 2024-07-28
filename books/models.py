from django.db import models

from authors.models import Author
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Book(models.Model):
    """ Модель книг """

    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.ForeignKey(Author, max_length=100, on_delete=models.CASCADE, verbose_name='Автор книги')
    written_year = models.IntegerField(**NULLABLE, verbose_name='год написание книги')
    genre = models.CharField(max_length=100, verbose_name='Жанр книги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'


class BookStatus(models.Model):
    """ Модель статуса книг """

    STATUS_CHOICES = [
        ('available', 'Доступна'),
        ('borrowed', 'Занята'),
        ('lost', 'Потеряна'),
    ]

    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, verbose_name='Статус книги')
    taken_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи киниги')
    returned_at = models.DateTimeField(**NULLABLE, verbose_name='Дата возвращение книги')

    def __str__(self):
        return f'{self.book} - {self.status}'

    class Meta:
        verbose_name = 'статус книги'
        verbose_name_plural = 'статусы книг'
