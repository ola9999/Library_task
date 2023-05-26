
""" helper class test """

from django.conf import settings
from django.urls import reverse
from django.test.client import encode_multipart

from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from apps.authlibrary.models import Client
from apps.book.models import Book,BorrowedBook

User = get_user_model()

class CreateUserMixin:

    @classmethod
    def create_user(cls, **params):
        """ create user with passed parameters and return the instance. """
        defaults = {
            'username': 'test',
            'password': 'pass',
            'email': 'test@email.com',
        }
        defaults.update(params)
        user = User.objects.create_user(**defaults)
        user.save()
        return user

class CreateClientUserBookTestMixin(CreateUserMixin):
    """
    Parent test classes ,
    holds the functionality of creation Clent object, Book object.
    """

    # pylint: disable=invalid-name
    @classmethod
    def setUpTestData(cls):
        # Guarantee first user existance
        cls.user = cls.create_user()
        # First book
        cls.book1 = cls.create_book()
        # First client
        cls.client1 = cls.create_client_user()
        # First client borrowing first book
        cls.borrowedbook1 = cls.create_borrowedbook()

    @classmethod
    def create_book(cls, **params):
        """Create and return a Book sample."""
        defaults = {
            'title':'title-test',
            'author':'author-test',
            'description':'description test',
            'is_active':True,
            'borrowing_price':15.00,
            'quantity':3,
        }
        defaults.update(params)

        book = Book.objects.create(**defaults)
        return book

    @classmethod
    def create_client_user(cls, **params):
        """Create and return a sample Client."""
        defaults = {
            'user_id':cls.user,
        }
        defaults.update(params)

        client_user = Client.objects.create(**defaults)
        return client_user


    @classmethod
    def create_borrowedbook(cls, **params):
        """Create and return a BorrowedBook sample."""
        defaults = {
            'client_id':cls.client1,
            'book_id':cls.book1,
        }
        defaults.update(params)

        borrowedbook = BorrowedBook.objects.create(**defaults)
        return borrowedbook


class CrudTestMixin(CreateUserMixin):

    # pylint: disable=invalid-name
    def setUp(self):
        """ To login before every test. """
        self.client = APIClient()
        self.client.login(**self.auth_cred)

    # pylint: disable=invalid-name
    @classmethod
    def setUpTestData(cls):
        # Default test user data for pass it to login client
        cls.auth_cred = {
            'username': 'test',
            'password': 'pass',
        }
        # test user
        cls.user = None

        # Create request data
        # Data attribues hold in needed data values to pass it in tests
        cls.create_data = None
        cls.update_data = None
        cls.delete_param = None

        # Common endpoint that will be calling in tests
        cls.list_endpoint = None
        cls.detail_endpoint = None
        cls.delete_endpoint = None

    def run_test_list(
        self,
        client,
        expected_status_code=status.HTTP_200_OK,
    ):
        response = client.get(self.list_endpoint)
        self.assertEqual(response.status_code, expected_status_code)

    def run_test_retrieve(
        self,
        client,
        expected_status_code=status.HTTP_200_OK,
    ):
        """
        Test retrieve  :
        get -> retrieve ->  Instance Detail test .
        """
        response = client.get(self.detail_endpoint)
        self.assertEqual(response.status_code, expected_status_code)

    def run_test_create(
            self,
            client,
            expected_status_code=status.HTTP_201_CREATED,
    ):
        """
        Create test :
        post -> create .
        """
        params = {
            'path': self.list_endpoint,
            'data': self.create_data,
            'format': 'multipart',
        }
        response = client.post(**params)
        self.assertEqual(response.status_code, expected_status_code)

    def run_test_update(
        self,
        client,
        expected_status_code=status.HTTP_200_OK,
    ):
        """
        Test update  :
        part update -> Update .
        """
        endpoint = self.detail_endpoint
        content = encode_multipart('BoUnDaRyStRiNg', self.update_data)
        content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'

        params = {
            'path': endpoint,
            'data': content,
            'content_type': content_type,
        }

        response = client.patch(**params)
        self.assertEqual(response.status_code, expected_status_code)

    def run_test_delete_with_custom_endpoint(
        self,
        client,
        endpoint,
        expected_status_code,
    ):
        """
        Test delete  :
        delete -> destroy .
        """
        response = client.delete(endpoint)
        self.assertEqual(response.status_code, expected_status_code)


class ListRetrieveTestMixin(CreateUserMixin):


    # pylint: disable=invalid-name
    def setUp(self):
        """ To login before every test. """
        self.client = APIClient()
        self.client.login(**self.auth_cred)

    # pylint: disable=invalid-name
    @classmethod
    def setUpTestData(cls):
        # Default test user data for pass it to login client
        cls.auth_cred = {
            'username': 'test',
            'password': 'pass',
        }
        # Default test user
        cls.user = None

        # Common endpoint that will be calling in tests
        cls.list_endpoint = None
        cls.detail_endpoint = None

    def run_test_list(
        self,
        client,
        expected_status_code=status.HTTP_200_OK,
    ):
        response = client.get(self.list_endpoint)
        print(response.json())
        # self.assertEqual(response.status_code, expected_status_code)

    def run_test_retrieve(
        self,
        client,
        expected_status_code=status.HTTP_200_OK,
    ):
        """
        Test retrieve  :
        get -> retrieve ->  Instance Detail test .
        """
        response = client.get(self.detail_endpoint)
        self.assertEqual(response.status_code, expected_status_code)
