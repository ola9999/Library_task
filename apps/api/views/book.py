from rest_framework.viewsets import (
    ModelViewSet,
    GenericViewSet,
    ReadOnlyModelViewSet,
)
from rest_framework import mixins
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


class BorrowedBookViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    """ 
    Viewset for borrowing book process .

    this viewset provides default `create()`, `retrieve()`,
    `destroy()` and `list()` actions.

    the client can't update the borrowing process !
    """
    queryset = BorrowedBook.objects.all()
    serializer_class = BorrowedBookSerializer


class UserBooksViewSet(
    ReadOnlyModelViewSet,
):
    queryset = Client.objects.all()
    serializer_class = UserBooksSerializer


class BookUsersViewSet(
    ReadOnlyModelViewSet,
):
    queryset = Book.objects.all()
    serializer_class = BookUsersSerializer
