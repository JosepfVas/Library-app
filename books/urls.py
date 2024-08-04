from django.urls import path

from books.views import (
    BookListAPIView,
    BookUpdateAPIView,
    BookRetrieveAPIView,
    BookDeleteAPIView,
    BookCreateAPIView,
    TakeBookView,
    ReturnBookView,
    BookStatusListAPIView,
)

urlpatterns = [
    # Book CRUD.
    path("list/", BookListAPIView.as_view(), name="book_list"),
    path("create/", BookCreateAPIView.as_view(), name="book_create"),
    path("update/<int:pk>/", BookUpdateAPIView.as_view(), name="book_update"),
    path("retrieve/<int:pk>/", BookRetrieveAPIView.as_view(), name="book_retrieve"),
    path("delete/<int:pk>/", BookDeleteAPIView.as_view(), name="book_delete"),
    # BookStatus CRUD.
    path("status-list/", BookStatusListAPIView.as_view(), name="book_status_list"),
    path(
        "status-retrieve/<int:pk>/",
        BookStatusListAPIView.as_view(),
        name="book_status_retrieve",
    ),
    path("take/<int:book_id>/", TakeBookView.as_view(), name="book_take"),
    path("return/<int:book_id>/", ReturnBookView.as_view(), name="book_return"),
]
