from django.urls import path
from .views import BookList, BookDetail, ClientList, ClientDetail

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('clients/', ClientList.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetail.as_view(), name='client-detail'),
]