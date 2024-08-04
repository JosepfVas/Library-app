from django.urls import path

from authors.views import (
    AuthorListAPIView,
    AuthorCreateAPIView,
    AuthorUpdateAPIView,
    AuthorRetrieveAPIView,
    AuthorDeleteAPIView,
)

urlpatterns = [
    path("list/", AuthorListAPIView.as_view(), name="author_list"),
    path("create/", AuthorCreateAPIView.as_view(), name="author_create"),
    path("update/<int:pk>/", AuthorUpdateAPIView.as_view(), name="author_update"),
    path("retrieve/<int:pk>/", AuthorRetrieveAPIView.as_view(), name="author_retrieve"),
    path("delete/<int:pk>/", AuthorDeleteAPIView.as_view(), name="author_delete"),
]
