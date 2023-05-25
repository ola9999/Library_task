from django.contrib import admin
from apps.book.models import Book,BorrowedBook


class BookAdmin(admin.ModelAdmin):

    list_display = (
        'title' ,
        'author' ,
        'description' ,
        'is_active' ,
    )

admin.site.register(Book, BookAdmin)


class BorrowedBookAdmin(admin.ModelAdmin):

    list_display = (
        'client' ,
        'book' ,
        'borrowed_date' ,
    )

    def client(self,obj):
        return obj.client.username

    def book(self,obj):
        return obj.book.title

admin.site.register(BorrowedBook, BorrowedBookAdmin)
