from books.permissions import IsModer, IsLibrarian
from users.models import User
from django.contrib.auth.models import Group
from users.permissions import IsAdmin, IsOwnerOrAdmin
from users.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)


# User Views
class UserCreateAPIView(CreateAPIView):
    """Создание пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

        reader_group = Group.objects.get(name='Readers')
        user.groups.add(reader_group)
        user.save()


class UserListAPIView(ListAPIView):
    """Список всех пользователей"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin | IsModer | IsLibrarian]


class UserRetrieveAPIView(RetrieveAPIView):
    """Вывод одного пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class UserUpdateAPIView(UpdateAPIView):
    """Обновление пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]


class UserDeleteAPIView(DestroyAPIView):
    """Удаление пользователя"""

    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdmin]
