from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Book

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_book_list(self):
        response = self.client.get('/books/')

        self.assertEqual(response.status_code, 200)

        soup=BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Books')
