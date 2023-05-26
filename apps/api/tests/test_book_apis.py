""" Test book app apis """

from django.utils import timezone

from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from apps.api.tests.utils import (
    CrudTestMixin,
    ListRetrieveTestMixin,
    CreateClientUserBookTestMixin,
)


class BookViewSetTest(
    CreateClientUserBookTestMixin,
    CrudTestMixin,
    TestCase,
):
    """
    Test class for News apis.
    """

    def setUp(self):
        return super().setUp()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CrudTestMixin().setUpTestData()
        cls.book_to_delete =cls.create_book(
            **{'title':'deleted book'},
        )

        # Common Endpoints
        cls.list_endpoint = reverse('book-list')
        cls.detail_endpoint =  reverse(
            'book-detail',
            kwargs={'pk': cls.book1.id}
        )
        cls.delete_endpoint = reverse(
            'book-detail',
            kwargs={'pk': cls.book_to_delete.id},
        )
        # Data creatiion
        cls.create_data = {
            'title':'title-test2',
            'author':'author-test2',
            'description':'description-test2',
            'is_active':True,
            'borrowing_price':15.00,
            'quantity':3,
        }
        cls.update_data = {
            'title':'updated-test',
        }

        cls.wrong_data = {
            'title':123,
        }

    def test_list(self):
        """
        List book test :
        get -> list.
        """
        self.run_test_list(self.client)

    def test_create(self):
        """
        Create book test :
        post -> create .
        """
        self.run_test_create(self.client)

    def test_retrieve(self):
        """
        Test retrieve book :
        get -> retrieve -> book Instance Detail test .
        """
        self.run_test_retrieve(self.client)

    def test_update(self):
        """
        Test update book :
        put -> Update .
        """
        self.run_test_update(self.client)

    def test_delete(self):
        """
        test delete book :
        delete -> destroy .
        """
        self.run_test_delete_with_custom_endpoint(
            self.client,
            self.delete_endpoint,
            status.HTTP_204_NO_CONTENT,
        )


class BorrowedBookViewSetTest(
    CreateClientUserBookTestMixin,
    CrudTestMixin,
    TestCase,
):
    """
    Test class for borrowed apis.
    """

    def setUp(self):
        return super().setUp()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CrudTestMixin().setUpTestData()
        cls.book2 =cls.create_book(
            **{'title':'book2 test'},
        )
        cls.book3 =cls.create_book(
            **{'title':'book3 test'},
        )
        cls.book4 =cls.create_book(
            **{'title':'book4 test'},
        )

        cls.borrowedbook_to_delete =cls.create_borrowedbook(
            **{
                'client_id':cls.client1,
                'book_id':cls.book2,
            },
        )
        
        # Common Endpoints
        cls.list_endpoint = reverse('borrowing-books-list')
        cls.detail_endpoint =  reverse(
            'borrowing-books-detail',
            kwargs={'pk': cls.borrowedbook1.id}
        )
        cls.delete_endpoint = reverse(
            'borrowing-books-detail',
            kwargs={'pk': cls.borrowedbook_to_delete.id},
        )
        # Data creatiion
        cls.create_data = {
            'client_id':cls.client1.id,
            'book_id':cls.book3.id,
        }
        cls.wrong_data = {
            'borrowed_date':timezone.now() - timezone.timedelta(minutes=60)
        }

    def test_list(self):
        """
        List Borrowedbook test :
        get -> list.
        """
        self.run_test_list(self.client)

    def test_create(self):
        """
        Create Borrowedbook test :
        post -> create .
        """
        self.run_test_create(self.client)

    def test_retrieve(self):
        """
        Test retrieve Borrowedbook :
        get -> retrieve -> Borrowedbook Instance Detail test .
        """
        self.run_test_retrieve(self.client)

    def test_delete(self):
        """
        test delete Borrowedbook :
        delete -> destroy .
        """
        self.run_test_delete_with_custom_endpoint(
            self.client,
            self.delete_endpoint,
            status.HTTP_204_NO_CONTENT,
        )



class UserBookViewSetTest(
    CreateClientUserBookTestMixin,
    ListRetrieveTestMixin,
    TestCase,
):
    """
    Test class for UserBookViewSet apis.
    """

    def setUp(self):
        return super().setUp()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        ListRetrieveTestMixin().setUpTestData()
        cls.book2 =cls.create_book(
            **{'title':'book2 test'},
        )
        cls.book3 =cls.create_book(
            **{'title':'book3 test'},
        )
        cls.book4 =cls.create_book(
            **{'title':'book4 test'},
        )

        cls.borrowedbook2 =cls.create_borrowedbook(
            **{
                'client_id':cls.client1,
                'book_id':cls.book2,
            },
        )
        cls.borrowedbook3 =cls.create_borrowedbook(
            **{
                'client_id':cls.client1,
                'book_id':cls.book3,
            },
        )
        cls.borrowedbook4 =cls.create_borrowedbook(
            **{
                'client_id':cls.client1,
                'book_id':cls.book4,
            },
        )
        
        # Common Endpoints
        cls.list_endpoint = reverse('user-books-list')
        cls.detail_endpoint =  reverse(
            'user-books-detail',
            kwargs={'pk': cls.client1.id}
        )

    def test_list(self):
        self.run_test_list(self.client)

    def test_retrieve(self):
        self.run_test_retrieve(self.client)


class BookUserViewSetTest(
    CreateClientUserBookTestMixin,
    ListRetrieveTestMixin,
    TestCase,
):
    """
    Test class for UserBookViewSet apis.
    """

    def setUp(self):
        return super().setUp()

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        CrudTestMixin().setUpTestData()
        cls.user2 = cls.create_user()
        cls.user3 = cls.create_user()
        cls.client2 = cls.create_client_user({
            'user_id':cls.user2.id,
        })
        cls.client3 = cls.create_client_user({
            'user_id':cls.user3.id,
        })

        cls.borrowedbook2 =cls.create_book(
            **{
                'client_id':cls.client1.id,
                'book_id':cls.book1.id,
            },
        )
        cls.borrowedbook3 =cls.create_book(
            **{
                'client_id':cls.client2.id,
                'book_id':cls.book1.id,
            },
        )
        cls.borrowedbook4 =cls.create_book(
            **{
                'client_id':cls.client3.id,
                'book_id':cls.book1.id,
            },
        )
        
        # Common Endpoints
        cls.list_endpoint = reverse('book-users-list')
        cls.detail_endpoint =  reverse(
            'book-users-detail',
            kwargs={'pk': cls.book1.id}
        )

    def test_list(self):
        self.run_test_list(self.client)

    def test_retrieve(self):
        self.run_test_retrieve(self.client)
