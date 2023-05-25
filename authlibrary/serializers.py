from rest_framework import serializers
from authlibrary.models import Book, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
