from rest_framework.viewsets import ModelViewSet
from apps.api.serializers.book import BookSerializer

from book.models import Book

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
