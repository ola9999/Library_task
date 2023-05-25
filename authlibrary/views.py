from rest_framework.viewsets import ModelViewSet

from authlibrary.models import Client
from authlibrary.serializers import ClientSerializer


class ClientViewset(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
