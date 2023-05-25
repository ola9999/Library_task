from rest_framework import serializers
from apps.authlibrary.models import Book

class BookSerializer(serializers.ModelSerializer):
    clients = serializers.StringRelatedField(many=True)

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

            'clients',
        ]
