from rest_framework import serializers
from apps.authlibrary.models import Client
from apps.api.serializers.book import BookSerializer


class ClientSerializer(serializers.ModelSerializer):
    books_borrowed = BookSerializer(
        many=True,
        read_only=True,
    )
    books_list_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Client
        fields = [
            'user',
            'book_borrowed',

            'books_borrowed',
            'books_list_ids',
        ]

        extra_kwargs = {
            'book_borrowed': {'write_only': True},
        }
