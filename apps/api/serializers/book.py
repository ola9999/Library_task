from rest_framework import serializers
from apps.book.models import Book,BorrowedBook


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'description',
            'is_active',
            'borrowing_price',
            'quantity',
        ]



class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = [
            'client',
            'book',
            'borrow_date',
        ]
