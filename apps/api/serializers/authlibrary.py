from rest_framework import serializers
from apps.authlibrary.models import Client



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id',
            'user',
        ]
