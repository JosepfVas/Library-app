from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from books.models import Book
from authors.models import Author


class BooksTestCase(APITestCase):
    """тесты на CRUD книг"""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com", password="test")
        self.author = Author.objects.create(fullname="Франц Кафка")
        self.book = Book.objects.create(
            title="замок",
            author=self.author,
            written_year=1926,
            genre="роман",
        )
        self.client.force_authenticate(user=self.user)

    def test_book_create(self):
        """Создание книги."""

        url = reverse("books:book_create")
        data = {
            "title": "замок",
            "author": 1,
            "written_year": 1926,
            "genre": "роман",
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_book_list(self):
        """Список книг"""

        url = reverse("books:book_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_retrieve(self):
        """Просмотр книги"""

        url = reverse("books:book_retrieve", args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], "замок")

    def test_book_update(self):
        """Обновление книги"""

        url = reverse("books:book_update", args=[self.book.id])
        data = {
            "title": "новое название",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book.id).title, "новое название")

    def test_book_delete(self):
        """Удаление книги"""

        url = reverse("books:book_delete", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)
