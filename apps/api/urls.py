from django.urls import path, include
from apps.api.views.authlibrary import ClientViewset
from apps.api.views.book import (
    BookViewSet,
    BookUsersViewSet,
    UserBooksViewSet,
    BorrowedBookViewSet,
)
from rest_framework import routers

# authlibrary app urls
client_router = routers.DefaultRouter()
client_router.register('', ClientViewset, basename='client')
client_router.register('user_books', UserBooksViewSet, basename='user-books')

# /user_books/ to list books related to a specific user
# /book_users/ to list users related to a specific book

# book app urls
book_router = routers.DefaultRouter()
book_router.register('', BookViewSet, basename='book')
# book_router.register('borrowing', BorrowedBookViewSet, basename='borrowing-books')
book_router.register('book_users', BookUsersViewSet, basename='book-users')

router = routers.DefaultRouter()

router.register('borrowing', BorrowedBookViewSet, basename='borrowing-books')

urlpatterns = [
    path('client/', include(client_router.urls)),
    path('book/', include(book_router.urls)),
    path('', include(router.urls)),
]
