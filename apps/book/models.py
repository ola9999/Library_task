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


class BorrowedBook(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.book.quantity > 0:
            self.book.quantity -= 1
            if self.book.quantity == 0:
                self.book.is_active = False
            self.book.save()
            super().save(*args, **kwargs)
        else:
            raise ValueError("Book is not available")
