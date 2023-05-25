from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import Book

class Client(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    books_borrowed = models.ManyToManyField(Book, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
