from rest_framework import serializers
from apps.authlibrary.models import Client
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )


class ClientSerializer(serializers.ModelSerializer):
    details = UserSerializer(
        read_only=True,
        source='user_id',
    )

    class Meta:
        model = Client
        fields = (
            'id',
            'user_id',
            # Extra fields
            'details',
        )




class RegisterClientSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for registering a new Client user.
    """
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = (
        'username',
        'password',
        )

    def create(self, validated_data):
        """
        Create a new user and AppRegisteration object.
        """
        password = validated_data.pop('password')
        user_data = {
            'username': validated_data['username'],
            'password': password,
        }
        user = get_user_model().objects.create_user(**user_data)
        user.set_password(password)
        user.save()

        ModelClass = self.Meta.model
        Client_obj = ModelClass._default_manager.create(
            user=user,
        )
        return Client_obj
