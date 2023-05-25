from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.api.serializers.book import BookSerializer
from apps.book.models import Book
from apps.book.models import BorrowedBook
from apps.api.serializers.book import (
    BookUsersSerializer,
    UserBooksSerializer,
    BorrowedBookSerializer,
)
from apps.authlibrary.models import Client


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowedBookViewSet(ModelViewSet):
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer


class UserBooksViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = UserBooksSerializer


class BookUsersViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookUsersSerializer
