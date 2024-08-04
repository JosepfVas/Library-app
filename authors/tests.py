from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from authors.models import Author


class AuthorsTestCase(APITestCase):
    """Тесты на CRUD автора"""

    def setUp(self):
        self.user = User.objects.create(email="test@example.com", password="test")
        self.author = Author.objects.create(
            fullname="Франц Кафка",
        )
        self.client.force_authenticate(user=self.user)

    def test_author_create(self):
        """Создание автора"""

        url = reverse("authors:author_create")
        data = {
            "fullname": "test",
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

    def test_author_list(self):
        """Список авторов"""

        url = reverse("authors:author_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_retrieve(self):
        """Просмотр автора"""

        url = reverse("authors:author_retrieve", args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["fullname"], "Франц Кафка")

    def test_author_update(self):
        """Обновление автора"""

        url = reverse("authors:author_update", args=[self.author.id])
        data = {
            "fullname": "test testov",
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Author.objects.get(pk=self.author.id).fullname, "test testov")

    def test_author_delete(self):
        """Удаление автора"""

        url = reverse("authors:author_delete", args=[self.author.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)
