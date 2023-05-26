from rest_framework import serializers
from apps.book.models import Book,BorrowedBook
from apps.authlibrary.models import Client
from apps.api.serializers.authlibrary import ClientSerializer


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

    def validate(self, attrs):
        if self.context['request'].method == 'POST':
            active= attrs.get('is_active',None)
            if not active:
                raise serializers.ValidationError(
                    "Book is not available",
                )
        return super().validate(attrs)


class BorrowedBookSerializer(serializers.ModelSerializer):
    """
    Serializers for make borrowing process
    """
    class Meta:
        model = BorrowedBook
        fields = [
            'client_id',
            'book_id',
            'borrowed_date',
        ]


class UserBooksSerializer(serializers.ModelSerializer):
    books = BookSerializer(
        many=True,
        read_only=True,
        source='borrowedbook_set.book_id',
    )
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = [
            'user_id',
            'books',
            # Extra fields
            'user_details',
        ]

    def get_user_details(self,obj):
        return ClientSerializer(obj).data

class BookUsersSerializer(serializers.ModelSerializer):
    users = ClientSerializer(
        many=True,
        read_only=True,
        source='borrowing_user_set.user_id.username',
    )
    book_details = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'users',
            # Extra fields
            'book_details',
        ]

    def get_book_details(self,obj):
        return BookSerializer(obj).data
