from django.urls import path, include
from apps.api.views.authlibrary import ClientViewset
from apps.api.views.book import BookViewSet

from rest_framework import routers

# authlibrary app urls
client_router = routers.DefaultRouter()
client_router.register('client', ClientViewset, basename='client')

# book app urls
book_router = routers.DefaultRouter()
book_router.register('book', BookViewSet, basename='book')

urlpatterns = [
    path('', include(client_router.urls)),
    path('', include(book_router.urls)),
]
