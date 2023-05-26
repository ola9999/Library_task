from django.db import models

from apps.authlibrary.models import Client

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    borrowing_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BorrowedBook(models.Model):
    client_id = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='borrowedbook_set',
    )
    book_id = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='borrowing_user_set',
    )
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client} borrowed {self.book}'

    def save(self, *args, **kwargs):
        if self.book_id.quantity > 0:
            self.book_id.quantity -= 1
            if self.book_id.quantity == 0:
                self.book_id.is_active = False
            self.book_id.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Book is not available")
