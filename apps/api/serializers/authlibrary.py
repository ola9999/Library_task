from rest_framework import serializers
from apps.authlibrary.models import Client
from django.contrib.auth import get_user_model

User = get_user_model()



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




class RegisterClientSerializer(
    serializers.ModelSerializer,
):
    """
    Serializer for registering a new Client user.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Client
        fields = [
        'username',
        'password',
        ]

    def create(self, validated_data):
        """
        Create a new user and AppRegisteration object.
        """
        password = validated_data.pop('password')
        user_data = {
            'username': validated_data['username'],
            'password': password,
        }
        user = User.objects.create_user(**user_data)
        user.set_password(password)
        user.save()

        ModelClass = self.Meta.model
        Client_obj = ModelClass._default_manager.create(
            user=user,
        )
        return Client_obj
