from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.api.serializers.book import BookSerializer

from apps.book.models import Book

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

        # book = self.get_object()
        # if book.borrow_book():
        #     serializer = self.get_serializer(book)
        #     return Response(serializer.data)
        # else:
        #     return Response(
        #         {
        #         'detail': 'This book is not available.'},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )
