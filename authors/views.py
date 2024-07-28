from rest_framework import generics
from authors.models import Author
from authors.serializers import AuthorSerializer


# CRUD для автора.

class AuthorCreateAPIView(generics.CreateAPIView):
    """ Создание автора """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorListAPIView(generics.ListAPIView):
    """ Список всех авторов """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного автора """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateAPIView(generics.UpdateAPIView):
    """ Обновление автора """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorDeleteAPIView(generics.DestroyAPIView):
    """ Удаление автора """

    queryset = Author.objects.all()
