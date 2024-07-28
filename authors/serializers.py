from rest_framework.serializers import ModelSerializer
from authors.models import Author


class AuthorSerializer(ModelSerializer):
    """ Сериализатор автора """

    class Meta:
        model = Author
        fields = "__all__"
