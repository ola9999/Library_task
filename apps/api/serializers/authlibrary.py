from rest_framework import serializers
from apps.authlibrary.models import Client



class ClientSerializer(serializers.ModelSerializer):
    username = serializers.PrimaryKeyRelatedField(
        source= 'user_id.username',
        read_only=True,
    )
    email = serializers.PrimaryKeyRelatedField(
        source= 'user_id.email',
        read_only=True,
    )

    class Meta:
        model = Client
        fields = [
            'id',
            'user_id',
            # Extra fields
            'username',
            'email',
        ]
