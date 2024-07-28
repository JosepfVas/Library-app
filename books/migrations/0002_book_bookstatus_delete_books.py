# Generated by Django 5.0.7 on 2024-07-28 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author'),
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('written_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата написание книги')),
                ('genre', models.CharField(max_length=100, verbose_name='Жанр книги')),
                ('author', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='authors.author', verbose_name='Автор книги')),
            ],
            options={
                'verbose_name': 'книга',
                'verbose_name_plural': 'книги',
            },
        ),
        migrations.CreateModel(
            name='BookStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('available', 'Доступна'), ('borrowed', 'Занята'), ('lost', 'Потеряна')], max_length=100, verbose_name='Статус книги')),
                ('issued_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выдачи киниги')),
                ('returned_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата возвращение книги')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book', verbose_name='Книга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'статус книги',
                'verbose_name_plural': 'статусы книг',
            },
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]
