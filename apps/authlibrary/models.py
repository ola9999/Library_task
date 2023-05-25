from django.conf import settings
from django.db import models
from apps.book.models import Book

class Client(models.Model):
    book_borrowed = models.ManyToManyField(
        Book,
        blank=True,
        related_name='book_set',
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        default=1,
        on_delete=models.CASCADE,
        related_name='client_user',
    )
