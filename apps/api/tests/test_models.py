""" test News model """

from django.core.exceptions import ValidationError
from django.test import TestCase
from apps.api.tests.utils import CreateClientUserBookTestMixin
from apps.authlibrary.models import Client
from apps.book.models import Book,BorrowedBook


class NewsAppTest(
    CreateClientUserBookTestMixin,
    TestCase,
):
    '''Class test for testing news app models'''

    @classmethod
    def setUpTestData(cls):
        """ Setup News model test data """
        super().setUpTestData()

        # Creation of Client :
        # Create image file.

        # Create audio file.

        cls.assertTrue(
            self=cls,
            expr=isinstance(cls.book1, Book),
        )
        cls.assertTrue(
            self=cls,
        )
        cls.assertTrue(
            self=cls,
            expr=isinstance(cls.borrowedbook1, BorrowedBook),
        )

    def test_client_creation(self):
        """ test the creation of client object """
        self.assertTrue(
            isinstance(self.client1, Client),
        )
        self.assertEqual(
            self.client1.__str__(),
            self.client1.user_id.username
        )

    def test_book_creation(self):
        """ test the creation of book object """
        self.assertTrue(
            isinstance(self.book1, Book),
        )
        self.assertEqual(
            self.book1.__str__(),
            self.book1.title,
        )

    def test_borrowedbook_creation(self):
        """ test the creation of borroedbook object """
        self.assertTrue(
            isinstance(self.borrowedbook1, BorrowedBook),
        )
        self.assertEqual(
            self.borrowedbook1.__str__(),
            f'{self.client1} borrowed {self.book1}',
        )
