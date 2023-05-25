from django.db import models

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

    def borrow_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            if self.quantity == 0:
                self.is_active = False
            self.save()
            return True
        return False
