from rest_framework import serializers
from authlibrary.models import Book, Client

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
