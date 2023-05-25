from rest_framework.viewsets import ModelViewSet
from apps.api.serializers.authlibrary import ClientSerializer
from authlibrary.models import Client



class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
