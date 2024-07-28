# Generated by Django 5.0.7 on 2024-07-28 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_bookstatus_delete_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='written_date',
        ),
        migrations.AddField(
            model_name='book',
            name='written_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='год написание книги'),
        ),
    ]
