from django.db import models

NULLABLE = {"blank": True, "null": True}


class Author(models.Model):
    """Модель автора"""

    fullname = models.CharField(
        max_length=150, **NULLABLE, verbose_name="Полное имя автора"
    )
    date_of_birth = models.IntegerField(**NULLABLE, verbose_name="Дата рождения")
    date_of_death = models.IntegerField(**NULLABLE, verbose_name="Дата смерти")
    biography = models.TextField(**NULLABLE, verbose_name="Биография писателя")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
