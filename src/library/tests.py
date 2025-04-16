from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book, Category, Publisher, Publication

class AuthorModelTest(TestCase):
    """Test cases for the Author model"""
    def setUp(self):
        """Create test author"""
        self.author = Author.objects.create(
            name="J.K. Rowling",
            birth_date="1965-07-31"
        )
